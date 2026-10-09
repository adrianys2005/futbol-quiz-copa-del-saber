const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const path = require('path');
const fs = require('fs');

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
  cors: { origin: '*' }
});

const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Data files paths
const questionsPath = path.join(__dirname, 'data', 'questions.json');
const teamsPath = path.join(__dirname, 'data', 'teams.json');

function loadJSON(filePath) {
  try {
    const raw = fs.readFileSync(filePath, 'utf-8');
    return JSON.parse(raw);
  } catch (err) {
    console.error(`Error loading ${filePath}:`, err);
    return [];
  }
}

function saveJSON(filePath, data) {
  try {
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
    return true;
  } catch (err) {
    console.error(`Error saving ${filePath}:`, err);
    return false;
  }
}

// Helper: Fisher-Yates shuffle
function fisherYatesShuffle(arr) {
  const result = [...arr];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}

// Helper: Randomize options A, B, C, D and recalculate correct index
function randomizeQuestionOptions(q) {
  if (!q || !Array.isArray(q.opciones) || q.correcta === undefined) return q;
  const correctText = q.opciones[q.correcta];
  const indices = [0, 1, 2, 3].slice(0, q.opciones.length);
  const shuffledIndices = fisherYatesShuffle(indices);
  const newOptions = shuffledIndices.map(idx => q.opciones[idx]);
  const newCorrectIndex = newOptions.indexOf(correctText);
  return {
    ...q,
    opciones: newOptions,
    correcta: newCorrectIndex >= 0 ? newCorrectIndex : q.correcta
  };
}

// Check subject compatibility
function matchesSubject(questionSubj, targetSubj) {
  if (!targetSubj || targetSubj === 'todas') return true;
  const qSubj = (questionSubj || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  const tSubj = (targetSubj || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');

  if (qSubj === tSubj) return true;
  if ((tSubj.includes('lenguaje') || tSubj.includes('lectura')) && (qSubj.includes('lenguaje') || qSubj.includes('lectura'))) return true;
  if ((tSubj.includes('sociales') || tSubj.includes('ciudadan')) && (qSubj.includes('sociales') || qSubj.includes('ciudadan'))) return true;
  if (tSubj.includes('naturales') && (qSubj.includes('naturales') || qSubj.includes('ambiental') || qSubj.includes('biologia'))) return true;
  if (tSubj.includes('matematica') && qSubj.includes('matematica')) return true;
  if (tSubj.includes('ingles') && qSubj.includes('ingles')) return true;
  return false;
}

// Smart question retrieval with adjacent grade fallback
function getFilteredQuestions(grado, asignatura) {
  const all = loadJSON(questionsPath);
  let pool = all;

  // Filter by subject
  if (asignatura && asignatura !== 'todas') {
    pool = pool.filter(q => matchesSubject(q.asignatura, asignatura));
  }

  if (!grado || grado === 'todos') {
    return pool.length > 0 ? pool : all;
  }

  // Exact grade match
  const targetGradeNum = parseInt(grado, 10);
  let gradeMatches = pool.filter(q => String(q.grado) === String(grado));

  // If grade has fewer than 8 questions for this subject, complement from adjacent grades
  if (gradeMatches.length < 8) {
    const existingIds = new Set(gradeMatches.map(q => q.id));
    // Sort pool questions by proximity of grade
    const candidates = pool
      .filter(q => !existingIds.has(q.id))
      .sort((a, b) => {
        const distA = Math.abs((parseInt(a.grado, 10) || targetGradeNum) - targetGradeNum);
        const distB = Math.abs((parseInt(b.grado, 10) || targetGradeNum) - targetGradeNum);
        return distA - distB;
      });

    for (const cand of candidates) {
      if (gradeMatches.length >= 15) break;
      gradeMatches.push(cand);
    }
  }

  return gradeMatches.length > 0 ? gradeMatches : all;
}

// REST API
app.get('/api/teams', (req, res) => {
  res.json(loadJSON(teamsPath));
});

app.get('/api/questions', (req, res) => {
  const { grado, asignatura } = req.query;
  const questions = getFilteredQuestions(grado, asignatura);
  res.json(questions);
});

app.post('/api/questions', (req, res) => {
  const newQuestion = req.body;
  if (!newQuestion.pregunta || !newQuestion.opciones || newQuestion.correcta === undefined) {
    return res.status(400).json({ error: 'Campos requeridos incompletos' });
  }
  const questions = loadJSON(questionsPath);
  newQuestion.id = newQuestion.id || `CUS-${Date.now().toString().slice(-5)}`;
  questions.push(newQuestion);
  saveJSON(questionsPath, questions);
  res.status(201).json({ success: true, question: newQuestion });
});

// Multiplayer Game Rooms State
// Room code -> { id, host, guest, settings: { grado, asignatura, maxGoals }, gameState }
const rooms = new Map();

function generateRoomCode() {
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let code = '';
  for (let i = 0; i < 6; i++) {
    code += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return code;
}

// io connection handlers

io.on('connection', (socket) => {
  console.log(`Cliente conectado: ${socket.id}`);

  // Create Room
  socket.on('create_room', (data) => {
    const { player, settings } = data;
    let roomCode = generateRoomCode();
    while (rooms.has(roomCode)) {
      roomCode = generateRoomCode();
    }

    const room = {
      code: roomCode,
      status: 'waiting', // waiting, ready, playing, finished
      settings: {
        grado: settings.grado || '11',
        asignatura: settings.asignatura || 'todas',
        maxGoals: settings.maxGoals || 3,
        timePerQuestion: 60
      },
      players: {
        host: {
          id: socket.id,
          name: player.name || 'Jugador 1',
          team: player.team,
          playerChar: player.playerChar,
          number: player.number || 10,
          score: 0,
          academicPoints: 0,
          ready: false
        },
        guest: null
      },
      matchState: null
    };

    rooms.set(roomCode, room);
    socket.join(roomCode);
    socket.roomCode = roomCode;
    socket.playerRole = 'host';

    socket.emit('room_created', {
      roomCode,
      room
    });
  });

  // Join Room
  socket.on('join_room', (data) => {
    const { roomCode, player } = data;
    const cleanCode = (roomCode || '').trim().toUpperCase();
    const room = rooms.get(cleanCode);

    if (!room) {
      return socket.emit('join_error', { message: 'Sala no encontrada. Revisa el código.' });
    }

    if (room.players.guest && room.players.guest.id !== socket.id) {
      return socket.emit('join_error', { message: 'La sala ya está llena.' });
    }

    room.players.guest = {
      id: socket.id,
      name: player.name || 'Jugador 2',
      team: player.team,
      playerChar: player.playerChar,
      number: player.number || 9,
      score: 0,
      academicPoints: 0,
      ready: false
    };

    room.status = 'ready';
    socket.join(cleanCode);
    socket.roomCode = cleanCode;
    socket.playerRole = 'guest';

    io.to(cleanCode).emit('player_joined', {
      roomCode: cleanCode,
      room
    });
  });

  // Player Ready
  socket.on('player_ready', () => {
    const room = rooms.get(socket.roomCode);
    if (!room) return;

    if (socket.playerRole === 'host') room.players.host.ready = true;
    if (socket.playerRole === 'guest') room.players.guest.ready = true;

    io.to(socket.roomCode).emit('room_updated', room);

    // If both ready, start match
    if (room.players.host?.ready && room.players.guest?.ready) {
      startMatch(room);
    }
  });

  function startMatch(room) {
    room.status = 'playing';
    const questions = getFilteredQuestions(room.settings.grado, room.settings.asignatura);
    
    // True Fisher-Yates shuffle and randomize option positions
    const shuffled = fisherYatesShuffle(questions).map(q => randomizeQuestionOptions(q));

    room.matchState = {
      ballPosition: 3, // 0 = P1 Goal, 3 = Center, 6 = P2 Goal
      turn: 'host', // 'host' or 'guest'
      possession: 'host',
      failedAttemptsInTurn: 0,
      recovererFailed: false,
      questions: shuffled,
      currentQuestionIndex: 0,
      history: []
    };

    io.to(room.code).emit('match_started', {
      room,
      currentQuestion: getSanitizedQuestion(room.matchState.questions[0])
    });
  }

  function getQuestionTimeLimit(q) {
    if (!q) return 60;
    const diff = (q.dificultad || '').toLowerCase();
    let baseTime = 60;

    if (diff.includes('difícil') || diff.includes('dificil') || diff.includes('avanzad')) {
      baseTime = 90; // 90s para preguntas difíciles
    } else if (diff.includes('fácil') || diff.includes('facil')) {
      baseTime = 45; // 45s para preguntas fáciles
    } else {
      baseTime = 65; // 65s para preguntas normales
    }

    const textLen = (q.pregunta || '').length;
    if (textLen > 200) {
      baseTime += 15;
    } else if (textLen > 130) {
      baseTime += 10;
    }

    return Math.min(120, Math.max(40, baseTime));
  }

  function getSanitizedQuestion(q) {
    if (!q) return null;
    return {
      id: q.id,
      grado: q.grado,
      asignatura: q.asignatura,
      tema: q.tema,
      pregunta: q.pregunta,
      opciones: q.opciones,
      dificultad: q.dificultad,
      fuente: q.fuente,
      tiempoLimite: getQuestionTimeLimit(q)
    };
  }

  // Answer Submitted in Multiplayer
  socket.on('submit_answer', (data) => {
    const room = rooms.get(socket.roomCode);
    if (!room || room.status !== 'playing' || !room.matchState) return;

    const role = socket.playerRole;
    const { answerIndex } = data;
    const match = room.matchState;

    // Verify it is this player's turn to answer
    if (match.turn !== role) return;

    const currentQ = match.questions[match.currentQuestionIndex];
    if (!currentQ) return;

    const isCorrect = answerIndex === currentQ.correcta;
    const explanation = currentQ.explicacion;

    let eventType = '';
    let goalScoredBy = null;

    if (isCorrect) {
      // Award academic points
      room.players[role].academicPoints += 100;
      match.recovererFailed = false;
      match.failedAttemptsInTurn = 0;

      // Ball Movement:
      // Host attacks towards position 6 (Guest's goal). Correct moves +1.
      // Guest attacks towards position 0 (Host's goal). Correct moves -1.
      if (role === 'host') {
        match.ballPosition += 1;
        if (match.ballPosition >= 6) {
          // GOL HOST!
          goalScoredBy = 'host';
          room.players.host.score += 1;
          match.ballPosition = 3; // Reset to center
          eventType = 'goal';
        } else {
          eventType = 'advance';
        }
      } else {
        match.ballPosition -= 1;
        if (match.ballPosition <= 0) {
          // GOL GUEST!
          goalScoredBy = 'guest';
          room.players.guest.score += 1;
          match.ballPosition = 3; // Reset to center
          eventType = 'goal';
        } else {
          eventType = 'advance';
        }
      }
      // Possession continues or alternates after goal
      match.possession = goalScoredBy ? (goalScoredBy === 'host' ? 'guest' : 'host') : role;
      match.turn = match.possession;

    } else {
      // INCORRECT ANSWER:
      // RF-011: Transfer opportunity to rival.
      // RF-012: If rival also answers incorrectly -> original recoverer recovers opportunity.
      // If recoverer fails again -> ball moves backward one position.
      if (match.failedAttemptsInTurn === 0) {
        // First failure: Interception by rival
        eventType = 'intercept';
        const rival = role === 'host' ? 'guest' : 'host';
        match.turn = rival;
        match.failedAttemptsInTurn = 1;
      } else if (match.failedAttemptsInTurn === 1) {
        // Rival also failed! Original team recovers
        eventType = 'recovered';
        const original = role === 'host' ? 'guest' : 'host';
        match.turn = original;
        match.failedAttemptsInTurn = 2;
        match.recovererFailed = true;
      } else {
        // Recoverer failed again! Ball moves backward one position (retreat toward own goal)
        eventType = 'retreat';
        if (role === 'host') {
          // Host retreats towards 0
          match.ballPosition = Math.max(1, match.ballPosition - 1);
        } else {
          // Guest retreats towards 6
          match.ballPosition = Math.min(5, match.ballPosition + 1);
        }
        // Change turn to break infinite loop
        match.turn = role === 'host' ? 'guest' : 'host';
        match.possession = match.turn;
        match.failedAttemptsInTurn = 0;
        match.recovererFailed = false;
      }
    }

    // Check Match Win Condition
    let matchWinner = null;
    if (room.players.host.score >= room.settings.maxGoals) {
      matchWinner = 'host';
      room.status = 'finished';
    } else if (room.players.guest.score >= room.settings.maxGoals) {
      matchWinner = 'guest';
      room.status = 'finished';
    }

    // Advance to next question
    match.currentQuestionIndex = (match.currentQuestionIndex + 1) % match.questions.length;
    const nextQ = match.questions[match.currentQuestionIndex];

    io.to(room.code).emit('round_result', {
      answeredBy: role,
      isCorrect,
      selectedAnswer: answerIndex,
      correctAnswer: currentQ.correcta,
      explanation,
      eventType,
      goalScoredBy,
      ballPosition: match.ballPosition,
      nextTurn: match.turn,
      scores: {
        host: room.players.host.score,
        guest: room.players.guest.score
      },
      academicPoints: {
        host: room.players.host.academicPoints,
        guest: room.players.guest.academicPoints
      },
      nextQuestion: getSanitizedQuestion(nextQ),
      matchWinner,
      status: room.status
    });
  });

  // Disconnection
  socket.on('disconnect', () => {
    console.log(`Cliente desconectado: ${socket.id}`);
    if (socket.roomCode) {
      const room = rooms.get(socket.roomCode);
      if (room) {
        io.to(socket.roomCode).emit('player_disconnected', {
          role: socket.playerRole,
          message: 'El oponente se ha desconectado.'
        });
        rooms.delete(socket.roomCode);
      }
    }
  });
});

server.listen(PORT, () => {
  console.log(`⚽ Servidor de Fútbol Quiz ejecutándose en http://localhost:${PORT}`);
});
