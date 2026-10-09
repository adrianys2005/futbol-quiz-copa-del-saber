/**
 * Fútbol Quiz: La Copa del Saber
 * Lógica principal del cliente, interfaz de usuario, modo individual y multijugador Socket.IO
 */

(function() {
  'use strict';

  // --- STATE ---
  const state = {
    teams: [],
    selectedTeam: null,
    selectedPlayer: null,
    selectedGrade: '11',
    questionMode: 'random', // 'random' | 'subject'
    selectedSubject: 'Matemáticas',
    gameMode: 'solo', // 'solo' | 'multi'
    socket: null,
    isMultiplayer: false,
    myRole: 'p1', // 'host' (p1) or 'guest' (p2)
    roomCode: null,

    // Match variables
    match: {
      active: false,
      ballPosition: 3, // 0 = P1 Goal, 3 = Centro, 6 = P2 Goal
      scoreP1: 0,
      scoreP2: 0,
      academicPoints: 0,
      turn: 'p1', // 'p1' (user) or 'p2' (cpu / guest)
      possession: 'p1',
      failedAttemptsInTurn: 0,
      questions: [],
      currentQuestionIndex: 0,
      currentQuestion: null,
      maxGoals: 3,
      timerSec: 25,
      timerId: null,
      canAnswer: false,
      stats: {
        total: 0,
        correct: 0,
        wrong: 0,
        subjects: {}
      }
    }
  };

  // --- DOM ELEMENTS ---
  const views = {
    welcome: document.getElementById('view-welcome'),
    customization: document.getElementById('view-customization'),
    grade: document.getElementById('view-grade'),
    questionsType: document.getElementById('view-questions-type'),
    gameMode: document.getElementById('view-game-mode'),
    multiLobby: document.getElementById('view-multiplayer-lobby'),
    match: document.getElementById('view-match'),
    results: document.getElementById('view-results')
  };

  function switchView(viewName) {
    Object.values(views).forEach(v => {
      if (v) v.classList.remove('active');
    });
    if (views[viewName]) {
      views[viewName].classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    const header = document.querySelector('.game-header');
    if (header) {
      header.style.display = (viewName === 'welcome') ? 'none' : 'flex';
    }
    const bgVideo = document.getElementById('welcome-video');
    if (bgVideo) {
      if (viewName === 'welcome') {
        bgVideo.play().catch(() => {});
      } else {
        bgVideo.pause();
      }
    }
  }

  // --- INITIALIZATION ---
  async function init() {
    setupHeaderButtons();
    setupModals();
    await loadTeams();
    setupCustomizationView();
    setupGradeView();
    setupQuestionTypeView();
    setupGameModeView();
    setupMultiplayerLobby();
    setupMatchView();
    setupResultsView();

    // Check if URL has ?room=ABC123
    const urlParams = new URLSearchParams(window.location.search);
    const roomParam = urlParams.get('room');
    if (roomParam) {
      document.getElementById('input-join-code').value = roomParam.toUpperCase();
      switchView('customization');
    } else {
      switchView('welcome');
    }
  }

  // --- HEADER & MODALS ---
  function setupHeaderButtons() {
    document.getElementById('btn-brand-home').addEventListener('click', () => {
      if (state.match.active) {
        if (confirm('¿Deseas salir del partido actual y volver al menú principal?')) {
          endCurrentMatch();
          switchView('welcome');
        }
      } else {
        switchView('welcome');
      }
    });

    const soundBtn = document.getElementById('btn-sound-toggle');
    const soundIcon = document.getElementById('sound-icon');
    const soundText = document.getElementById('sound-text');
    soundBtn.addEventListener('click', () => {
      const isEnabled = window.sounds.toggle();
      soundIcon.textContent = isEnabled ? '🔊' : '🔇';
      soundText.textContent = isEnabled ? 'Audio' : 'Mudo';
    });

    document.getElementById('btn-open-instructions').addEventListener('click', () => {
      openModal('modal-instructions');
    });

    function showWelcomeToast(msg) {
      let toast = document.getElementById('welcome-toast-badge');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'welcome-toast-badge';
        toast.style.cssText = `
          position: fixed;
          top: 30px;
          left: 50%;
          transform: translateX(-50%) translateY(-20px);
          background: rgba(15, 23, 42, 0.95);
          color: #facc15;
          font-weight: 800;
          font-size: 1rem;
          padding: 10px 24px;
          border-radius: 999px;
          border: 1px solid #facc15;
          box-shadow: 0 8px 30px rgba(0,0,0,0.8), 0 0 20px rgba(250,204,21,0.4);
          z-index: 10005;
          pointer-events: none;
          opacity: 0;
          transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        `;
        document.body.appendChild(toast);
      }
      toast.textContent = msg;
      toast.style.opacity = '1';
      toast.style.transform = 'translateX(-50%) translateY(0)';
      clearTimeout(window._toastTimer);
      window._toastTimer = setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(-50%) translateY(-20px)';
      }, 2200);
    }
    
    const welcomeSoundBtn = document.getElementById('btn-sound-welcome');
    if (welcomeSoundBtn) {
      welcomeSoundBtn.addEventListener('click', () => {
        const isEnabled = window.sounds.toggle();
        soundIcon.textContent = isEnabled ? '🔊' : '🔇';
        soundText.textContent = isEnabled ? 'Audio' : 'Mudo';
        const welcomeLabel = document.getElementById('welcome-sound-label');
        const welcomeIcon = welcomeSoundBtn.querySelector('.welcome-top-icon');
        if (welcomeLabel) welcomeLabel.textContent = isEnabled ? 'Audio' : 'Mudo';
        if (welcomeIcon) welcomeIcon.textContent = isEnabled ? '🔊' : '🔇';
        if (isEnabled) {
          window.sounds.playKick();
          showWelcomeToast('🔊 Audio Activado');
        } else {
          showWelcomeToast('🔇 Audio Silenciado');
        }
      });
    }

    const welcomeRulesBtn = document.getElementById('btn-rules-welcome');
    if (welcomeRulesBtn) {
      welcomeRulesBtn.addEventListener('click', () => {
        window.sounds.playKick();
        openModal('modal-instructions');
      });
    }

    const instWelcome = document.getElementById('btn-inst-welcome');
    if (instWelcome) {
      instWelcome.addEventListener('click', () => {
        window.sounds.playKick();
        openModal('modal-instructions');
      });
    }

    const credWelcome = document.getElementById('btn-credits-welcome');
    if (credWelcome) {
      credWelcome.addEventListener('click', () => {
        window.sounds.playKick();
        openModal('modal-credits');
      });
    }

    const startGameBtn = document.getElementById('btn-start-game');
    if (startGameBtn) {
      startGameBtn.addEventListener('click', () => {
        window.sounds.playWhistle();
        switchView('customization');
      });
    }
  }

  function openModal(id) {
    const modal = document.getElementById(id);
    if (modal) modal.classList.add('open');
  }

  function closeModal(id) {
    const modal = document.getElementById(id);
    if (modal) modal.classList.remove('open');
  }

  function setupModals() {
    document.getElementById('btn-close-instructions').addEventListener('click', () => {
      closeModal('modal-instructions');
    });
    document.getElementById('btn-close-credits').addEventListener('click', () => {
      closeModal('modal-credits');
    });

    window.addEventListener('click', (e) => {
      if (e.target.classList.contains('modal-backdrop')) {
        e.target.classList.remove('open');
      }
    });
  }

  // --- 1. LOAD TEAMS & PLAYERS ---
  async function loadTeams() {
    try {
      const res = await fetch('/api/teams');
      state.teams = await res.json();
      if (state.teams.length > 0) {
        state.selectedTeam = state.teams[0]; // Default Colombia
        state.selectedPlayer = state.selectedTeam.players[0];
      }
    } catch (err) {
      console.error('Error fetching teams:', err);
      // Fallback
      state.teams = [
        {
          id: 'colombia',
          name: 'Colombia',
          code: 'CO',
          flag: '🇨🇴',
          players: [{ name: 'James Rodríguez', number: 10, role: 'Centrocampista', avatar: '⭐' }]
        }
      ];
      state.selectedTeam = state.teams[0];
      state.selectedPlayer = state.selectedTeam.players[0];
    }
  }

  // --- 2. CUSTOMIZATION VIEW (EXACTO A LA IMAGEN "PASO 1 DE 4") ---
  function getFederationCrestSVG(fedOrId) {
    const id = (fedOrId || '').toLowerCase();
    if (id.includes('afa') || id.includes('argentina') || id === 'ar') {
      return `
        <svg viewBox="0 0 100 110" width="70" height="77" class="fed-crest-svg">
          <!-- 3 Estrellas Doradas AFA -->
          <polygon points="26,6 29,14 37,14 31,19 33,27 26,22 19,27 21,19 15,14 23,14" fill="#facc15" filter="drop-shadow(0 0 3px #eab308)"/>
          <polygon points="50,2 53,10 61,10 55,15 57,23 50,18 43,23 45,15 39,10 47,10" fill="#facc15" filter="drop-shadow(0 0 4px #eab308)"/>
          <polygon points="74,6 77,14 85,14 79,19 81,27 74,22 67,27 69,19 63,14 71,14" fill="#facc15" filter="drop-shadow(0 0 3px #eab308)"/>
          <!-- Escudo AFA -->
          <path d="M20,30 L80,30 C80,68 62,94 50,102 C38,94 20,68 20,30 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
          <path d="M26,34 L74,34 C74,64 59,88 50,94 C41,88 26,64 26,34 Z" fill="#ffffff"/>
          <rect x="36" y="34" width="9" height="52" fill="#75aadb"/>
          <rect x="55" y="34" width="9" height="52" fill="#75aadb"/>
          <text x="50" y="66" font-size="20" font-weight="900" fill="#1e3a8a" text-anchor="middle" letter-spacing="1">AFA</text>
        </svg>`;
    }
    if (id.includes('fcf') || id.includes('colombia') || id === 'co') {
      return `
        <svg viewBox="0 0 100 110" width="70" height="77" class="fed-crest-svg">
          <circle cx="50" cy="55" r="42" fill="#0f172a" stroke="#facc15" stroke-width="3"/>
          <circle cx="50" cy="55" r="36" fill="#fcd116"/>
          <path d="M14,55 A36,36 0 0,0 86,55 Z" fill="#003893"/>
          <path d="M22,70 A36,36 0 0,0 78,70 Z" fill="#ce1126"/>
          <circle cx="50" cy="55" r="16" fill="#ffffff" stroke="#ce1126" stroke-width="2"/>
          <text x="50" y="61" font-size="14" font-weight="900" fill="#003893" text-anchor="middle">FCF</text>
        </svg>`;
    }
    if (id.includes('fff') || id.includes('francia') || id.includes('france') || id === 'fr') {
      return `
        <svg viewBox="0 0 100 110" width="70" height="77" class="fed-crest-svg">
          <!-- 2 Estrellas Doradas FFF -->
          <polygon points="36,4 39,12 47,12 41,17 43,25 36,20 29,25 31,17 25,12 33,12" fill="#facc15"/>
          <polygon points="64,4 67,12 75,12 69,17 71,25 64,20 57,25 59,17 53,12 61,12" fill="#facc15"/>
          <polygon points="50,28 85,46 85,82 50,102 15,82 15,46" fill="#002395" stroke="#facc15" stroke-width="2.5"/>
          <text x="50" y="66" font-size="28" text-anchor="middle">🐓</text>
          <text x="50" y="90" font-size="14" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="1">FFF</text>
        </svg>`;
    }
    if (id.includes('fpf') || id.includes('portugal') || id === 'pt') {
      return `
        <svg viewBox="0 0 100 110" width="70" height="77" class="fed-crest-svg">
          <path d="M20,18 L80,18 C80,65 62,95 50,102 C38,95 20,65 20,18 Z" fill="#da291c" stroke="#facc15" stroke-width="3"/>
          <rect x="42" y="24" width="16" height="66" fill="#ffffff"/>
          <rect x="25" y="44" width="50" height="16" fill="#ffffff"/>
          <circle cx="50" cy="52" r="14" fill="#046a38" stroke="#facc15" stroke-width="2"/>
          <text x="50" y="57" font-size="12" font-weight="900" fill="#facc15" text-anchor="middle">FPF</text>
        </svg>`;
    }
    // Alemania (DFB)
    return `
      <svg viewBox="0 0 100 110" width="70" height="77" class="fed-crest-svg">
        <!-- 4 Estrellas Doradas DFB -->
        <polygon points="20,8 22,14 28,14 23,18 25,24 20,20 15,24 17,18 12,14 18,14" fill="#facc15"/>
        <polygon points="40,4 42,10 48,10 43,14 45,20 40,16 35,20 37,14 32,10 38,10" fill="#facc15"/>
        <polygon points="60,4 62,10 68,10 63,14 65,20 60,16 55,20 57,14 52,10 58,10" fill="#facc15"/>
        <polygon points="80,8 82,14 88,14 83,18 85,24 80,20 75,24 77,18 72,14 78,14" fill="#facc15"/>
        <circle cx="50" cy="60" r="38" fill="#111111" stroke="#facc15" stroke-width="2.5"/>
        <circle cx="50" cy="60" r="30" fill="#ffffff"/>
        <text x="50" y="67" font-size="26" text-anchor="middle">🦅</text>
        <text x="50" y="85" font-size="11" font-weight="900" fill="#111111" text-anchor="middle" letter-spacing="1">DFB</text>
      </svg>`;
  }

  function setupCustomizationView() {
    const teamsContainer = document.getElementById('teams-selector-container');
    const playersContainer = document.getElementById('players-selector-container');

    // 1. Renderizar las 5 Selecciones en la Fila Superior
    function renderTeams() {
      if (!teamsContainer) return;
      teamsContainer.innerHTML = '';

      state.teams.forEach(team => {
        const isSelected = (state.selectedTeam.id === team.id);
        const card = document.createElement('div');
        card.className = `step1-team-card ${isSelected ? 'selected' : ''}`;
        card.dataset.team = team.id;
        
        card.innerHTML = `
          <div class="team-card-crest-box">
            ${getFederationCrestSVG(team.federation || team.id)}
          </div>
          <div class="team-card-name-label">
            <span class="team-card-flag">${team.flag || ''}</span>
            <span class="team-card-title">${team.name.toUpperCase()}</span>
          </div>
        `;

        card.addEventListener('click', () => {
          state.selectedTeam = team;
          state.selectedPlayer = team.players[0];
          window.sounds.playKick();
          renderTeams();
          updateCountryInfo();
          renderPlayers();
          updateStatusPill();
        });

        teamsContainer.appendChild(card);
      });
    }

    // 2. Actualizar el Panel Izquierdo con los datos de la Selección Activa
    function updateCountryInfo() {
      const team = state.selectedTeam;
      if (!team) return;

      const flagEl = document.getElementById('country-flag-display');
      const nameEl = document.getElementById('country-name-display');
      const descEl = document.getElementById('country-desc-display');
      const crestEl = document.getElementById('country-federation-display');
      const titleEl = document.getElementById('roster-title-display');

      if (flagEl) flagEl.textContent = team.flag || '⚽';
      if (nameEl) nameEl.textContent = team.name.toUpperCase();
      if (descEl) descEl.textContent = team.description || `Una selección llena de talento, técnica y pasión. ¡Lleva a ${team.name} a la gloria!`;
      if (crestEl) crestEl.innerHTML = getFederationCrestSVG(team.federation || team.id);
      if (titleEl) titleEl.textContent = `JUGADORES DE ${team.name.toUpperCase()} (${team.players ? team.players.length : 5})`;
    }

    // 3. Renderizar los Jugadores Oficiales de la Selección (5 Jugadores)
    function renderPlayers() {
      if (!playersContainer || !state.selectedTeam || !state.selectedTeam.players) return;
      playersContainer.innerHTML = '';

      const team = state.selectedTeam;

      // 5 Jugadores Oficiales de la Selección
      team.players.forEach(p => {
        const isSelected = (state.selectedPlayer && state.selectedPlayer.name === p.name);
        const card = document.createElement('div');
        card.className = `step1-player-card ${isSelected ? 'selected' : ''}`;

        let roleClass = 'pill-fw';
        const roleLower = (p.role || '').toLowerCase();
        if (roleLower.includes('medio') || roleLower.includes('volante') || roleLower.includes('centro')) roleClass = 'pill-mf';
        else if (roleLower.includes('defens') || roleLower.includes('lateral')) roleClass = 'pill-df';
        else if (roleLower.includes('porter') || roleLower.includes('arquer')) roleClass = 'pill-gk';

        card.innerHTML = `
          <!-- 4 Brackets de Selección estilo Romero (Imagen 1) -->
          <div class="fut-selection-bracket bracket-tl"></div>
          <div class="fut-selection-bracket bracket-tr"></div>
          <div class="fut-selection-bracket bracket-bl"></div>
          <div class="fut-selection-bracket bracket-br"></div>

          <!-- Valoración y Posición Superior Izquierda -->
          <div class="step1-card-top-left">
            <span class="p-rating">${p.rating || 88}</span>
            <span class="p-pos">${p.pos || 'ST'}</span>
          </div>

          <!-- Foto del Jugador -->
          <div class="step1-card-photo-box">
            <img src="${p.image || team.image || 'assets/banner.jpg'}" alt="${p.name}" class="step1-card-img" onerror="this.src='${team.image || 'assets/banner.jpg'}'">
          </div>

          <!-- Nombre del Jugador -->
          <div class="step1-card-name">${p.shortName || p.name}</div>

          <!-- 6 Atributos FIFA -->
          <div class="step1-card-stats">
            <div class="stat-col"><strong>${p.stats?.pac || 85}</strong><span>PAC</span></div>
            <div class="stat-col"><strong>${p.stats?.sho || 85}</strong><span>SHO</span></div>
            <div class="stat-col"><strong>${p.stats?.pas || 85}</strong><span>PAS</span></div>
            <div class="stat-col"><strong>${p.stats?.dri || 85}</strong><span>DRI</span></div>
            <div class="stat-col"><strong>${p.stats?.def || 85}</strong><span>DEF</span></div>
            <div class="stat-col"><strong>${p.stats?.phy || 85}</strong><span>PHY</span></div>
          </div>

          <!-- Dorsal de Camiseta -->
          <div class="step1-card-number-badge">#${p.number}</div>

          <!-- Rol Táctico -->
          <div class="step1-role-pill ${roleClass}">${p.role || 'Delantero'}</div>
        `;

        card.addEventListener('click', () => {
          state.selectedPlayer = p;
          window.sounds.playKick();
          renderPlayers();
          updateStatusPill();
        });

        playersContainer.appendChild(card);
      });
    }

    // 4. Actualizar la Pastilla Inferior de Estado
    function updateStatusPill() {
      const statusText = document.getElementById('status-text-display');
      if (statusText && state.selectedPlayer) {
        statusText.innerHTML = `⭐ <strong>${state.selectedPlayer.name}</strong> seleccionado | Dorsal #${state.selectedPlayer.number} (${state.selectedPlayer.role || 'Figura'})`;
      }
    }

    // Inicializar vistas
    renderTeams();
    updateCountryInfo();
    renderPlayers();
    updateStatusPill();

    // Toggle roster button
    const btnToggle = document.getElementById('btn-toggle-roster-view');
    if (btnToggle) {
      btnToggle.addEventListener('click', () => {
        playersContainer?.scrollIntoView({ behavior: 'smooth' });
      });
    }

    // Botones de Navegación
    const btnBack = document.getElementById('btn-back-to-welcome');
    if (btnBack) {
      btnBack.addEventListener('click', () => {
        switchView('welcome');
      });
    }

    const btnNext = document.getElementById('btn-next-to-grade');
    if (btnNext) {
      btnNext.addEventListener('click', () => {
        const nameInput = document.getElementById('player-name-input');
        const alias = nameInput ? nameInput.value.trim() : 'Goleador';
        if (!alias) {
          alert('Por favor escribe tu nombre o apodo.');
          return;
        }
        window.sounds.playKick();
        switchView('grade');
      });
    }
  }

  // --- 3. GRADE VIEW (IMAGEN 2 "PASO 2 DE 4: ELIGE TU CATEGORÍA") ---
  function setupGradeView() {
    const gradeCards = document.querySelectorAll('.fut-grade-card, .grade-btn');
    gradeCards.forEach(card => {
      card.addEventListener('click', () => {
        const grade = card.dataset.grade || '11';
        gradeCards.forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
        state.selectedGrade = grade;
        window.sounds.playKick();
      });
    });

    const btnBack = document.getElementById('btn-back-to-custom');
    if (btnBack) {
      btnBack.addEventListener('click', () => {
        switchView('customization');
      });
    }

    const btnNext = document.getElementById('btn-next-to-question-type');
    if (btnNext) {
      btnNext.addEventListener('click', () => {
        window.sounds.playKick();
        switchView('questionsType');
      });
    }
  }

  // --- 4. QUESTION TYPE VIEW (IMAGEN 3 "PASO 3 DE 4: Modalidad de Preguntas") ---
  function setupQuestionTypeView() {
    const randomCard = document.getElementById('choice-random-mode');
    const subjectCard = document.getElementById('choice-subject-mode');
    const subjectPanel = document.getElementById('subject-selection-panel');
    const chips = document.querySelectorAll('.fut-subject-badge, .subject-chip');

    const randomBadge = randomCard ? randomCard.querySelector('.hud-card-badge-top') : null;
    const subjectBadge = subjectCard ? subjectCard.querySelector('.hud-card-badge-top') : null;

    if (randomCard) {
      randomCard.addEventListener('click', () => {
        randomCard.classList.add('selected');
        if (subjectCard) subjectCard.classList.remove('selected');
        if (randomBadge) randomBadge.style.display = 'block';
        if (subjectBadge) subjectBadge.style.display = 'none';
        if (subjectPanel) subjectPanel.style.display = 'none';
        state.questionMode = 'random';
        window.sounds.playKick();
      });
    }

    if (subjectCard) {
      subjectCard.addEventListener('click', () => {
        subjectCard.classList.add('selected');
        if (randomCard) randomCard.classList.remove('selected');
        if (subjectBadge) subjectBadge.style.display = 'block';
        if (randomBadge) randomBadge.style.display = 'none';
        if (subjectPanel) subjectPanel.style.display = 'block';
        state.questionMode = 'subject';
        window.sounds.playKick();
      });
    }

    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        chips.forEach(c => c.classList.remove('selected'));
        chip.classList.add('selected');
        state.selectedSubject = chip.dataset.subject;
        window.sounds.playKick();
      });
    });

    const btnBack = document.getElementById('btn-back-to-grade');
    if (btnBack) {
      btnBack.addEventListener('click', () => {
        switchView('grade');
      });
    }

    const btnNext = document.getElementById('btn-next-to-gamemode');
    if (btnNext) {
      btnNext.addEventListener('click', () => {
        window.sounds.playKick();
        switchView('gameMode');
      });
    }
  }

  // --- 5. GAME MODE VIEW (IMAGEN 3 "PASO 4 DE 4: Modo de Juego") ---
  function setupGameModeView() {
    const soloCard = document.getElementById('choice-solo-game');
    const multiCard = document.getElementById('choice-multi-game');
    const soloBadge = soloCard ? soloCard.querySelector('.hud-card-badge-top') : null;
    const multiBadge = multiCard ? multiCard.querySelector('.hud-card-badge-top') : null;

    if (soloCard) {
      soloCard.addEventListener('click', () => {
        soloCard.classList.add('selected');
        if (multiCard) multiCard.classList.remove('selected');
        if (soloBadge) soloBadge.style.display = 'block';
        if (multiBadge) multiBadge.style.display = 'none';
        state.gameMode = 'solo';
        window.sounds.playKick();
      });
    }

    if (multiCard) {
      multiCard.addEventListener('click', () => {
        multiCard.classList.add('selected');
        if (soloCard) soloCard.classList.remove('selected');
        if (multiBadge) multiBadge.style.display = 'block';
        if (soloBadge) soloBadge.style.display = 'none';
        state.gameMode = 'multi';
        window.sounds.playKick();
      });
    }

    const btnBack = document.getElementById('btn-back-to-qtype');
    if (btnBack) {
      btnBack.addEventListener('click', () => {
        switchView('questionsType');
      });
    }

    const btnLaunch = document.getElementById('btn-launch-mode');
    if (btnLaunch) {
      btnLaunch.addEventListener('click', () => {
        window.sounds.playWhistle();
        if (state.gameMode === 'solo') {
          startSoloMatch();
        } else {
          openMultiplayerLobby();
        }
      });
    }
  }

  // --- 6. MULTIPLAYER ONLINE LOBBY (SOCKET.IO) ---
  function initSocket() {
    if (!state.socket && typeof io !== 'undefined') {
      state.socket = io();

      state.socket.on('room_created', (data) => {
        state.roomCode = data.roomCode;
        state.myRole = 'host';
        document.getElementById('display-room-code').textContent = data.roomCode;
        
        // Render QR
        const roomUrl = `${window.location.origin}${window.location.pathname}?room=${data.roomCode}`;
        window.generateQRCode('qrcode-box', roomUrl, 180);

        // Update lobby UI
        document.getElementById('lobby-host-name').textContent = `${data.room.players.host.name} (${data.room.players.host.team.name})`;
        document.getElementById('lobby-host-avatar').textContent = data.room.players.host.playerChar.avatar;
      });

      state.socket.on('player_joined', (data) => {
        const guest = data.room.players.guest;
        if (guest) {
          document.getElementById('lobby-guest-name').textContent = `${guest.name} (${guest.team.name})`;
          document.getElementById('lobby-guest-avatar').textContent = guest.playerChar.avatar;
          const statusSpan = document.getElementById('lobby-guest-status');
          statusSpan.textContent = 'Conectado';
          statusSpan.className = 'vs-status ready';

          const startBtn = document.getElementById('btn-start-multi-match');
          startBtn.disabled = false;
          startBtn.style.opacity = '1';
          startBtn.textContent = '¡Iniciar Partido Ahora! ⚽';
        }
      });

      state.socket.on('join_error', (data) => {
        alert(data.message || 'Error al unirse a la sala.');
      });

      state.socket.on('match_started', (data) => {
        startMultiMatchClient(data);
      });

      state.socket.on('round_result', (data) => {
        handleMultiRoundResult(data);
      });

      state.socket.on('player_disconnected', (data) => {
        alert(data.message);
        endCurrentMatch();
        switchView('welcome');
      });
    }
  }

  function setupMultiplayerLobby() {
    const tabCreate = document.getElementById('tab-create-room');
    const tabJoin = document.getElementById('tab-join-room');
    const panelCreate = document.getElementById('panel-create-room');
    const panelJoin = document.getElementById('panel-join-room');

    tabCreate.addEventListener('click', () => {
      tabCreate.classList.add('active');
      tabJoin.classList.remove('active');
      panelCreate.style.display = 'block';
      panelJoin.style.display = 'none';
      createRoomOnServer();
    });

    tabJoin.addEventListener('click', () => {
      tabJoin.classList.add('active');
      tabCreate.classList.remove('active');
      panelCreate.style.display = 'none';
      panelJoin.style.display = 'block';
    });

    document.getElementById('btn-copy-room-link').addEventListener('click', () => {
      if (!state.roomCode) return;
      const roomUrl = `${window.location.origin}${window.location.pathname}?room=${state.roomCode}`;
      navigator.clipboard.writeText(`¡Juega conmigo a Fútbol Quiz! Código: ${state.roomCode} o entra en: ${roomUrl}`).then(() => {
        alert('¡Código y enlace de la sala copiados al portapapeles!');
      });
    });

    document.getElementById('btn-submit-join').addEventListener('click', () => {
      const code = document.getElementById('input-join-code').value.trim().toUpperCase();
      if (!code) {
        alert('Por favor ingresa un código de sala.');
        return;
      }
      joinRoomOnServer(code);
    });

    document.getElementById('btn-start-multi-match').addEventListener('click', () => {
      if (state.socket) {
        state.socket.emit('player_ready');
      }
    });

    document.getElementById('btn-cancel-lobby').addEventListener('click', () => {
      switchView('gameMode');
    });
  }

  function openMultiplayerLobby() {
    initSocket();
    switchView('multiLobby');
    createRoomOnServer();
  }

  function getMyPlayerData() {
    const name = document.getElementById('player-name-input').value.trim() || 'Jugador';
    return {
      name,
      team: state.selectedTeam,
      playerChar: state.selectedPlayer,
      number: state.selectedPlayer.number
    };
  }

  function createRoomOnServer() {
    if (!state.socket) return;
    const player = getMyPlayerData();
    state.socket.emit('create_room', {
      player,
      settings: {
        grado: state.selectedGrade,
        asignatura: state.questionMode === 'subject' ? state.selectedSubject : 'todas',
        maxGoals: 3
      }
    });
  }

  function joinRoomOnServer(code) {
    if (!state.socket) return;
    state.myRole = 'guest';
    const player = getMyPlayerData();
    state.socket.emit('join_room', {
      roomCode: code,
      player
    });
  }

  // --- 7. MATCH ENGINE (CANCHA & PREGUNTAS) ---
  // --- 7. MATCH ENGINE (CANCHA, PERSONAJES & PREGUNTAS) ---
  function setupMatchView() {
    const answerButtons = document.querySelectorAll('.answer-option-btn');
    answerButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        if (!state.match.canAnswer) return;
        const answerIndex = parseInt(btn.dataset.index, 10);
        submitAnswer(answerIndex);
      });
    });

    // Botón de Cancelar Partido
    const btnCancel = document.getElementById('btn-cancel-match');
    const modalCancel = document.getElementById('modal-cancel-confirm');
    const btnCancelYes = document.getElementById('btn-cancel-dialog-yes');
    const btnCancelNo = document.getElementById('btn-cancel-dialog-no');

    if (btnCancel) {
      btnCancel.addEventListener('click', () => {
        if (modalCancel) modalCancel.classList.add('open');
      });
    }

    if (btnCancelNo) {
      btnCancelNo.addEventListener('click', () => {
        if (modalCancel) modalCancel.classList.remove('open');
      });
    }

    if (btnCancelYes) {
      btnCancelYes.addEventListener('click', () => {
        if (modalCancel) modalCancel.classList.remove('open');
        endCurrentMatch();
        switchView('welcome');
      });
    }

    // Botones de Pausa de Partido (Solo para Partida Individual / Offline)
    const btnPause = document.getElementById('btn-pause-match');
    const modalPause = document.getElementById('modal-pause');
    const btnResume = document.getElementById('btn-resume-match');
    const btnRestart = document.getElementById('btn-restart-match');
    const btnExitMenu = document.getElementById('btn-exit-to-menu');

    if (btnPause) {
      btnPause.addEventListener('click', () => {
        if (!state.match.active || state.isMultiplayer) return;
        state.match.isPaused = true;
        clearInterval(state.match.timerId);
        const phaseText = document.getElementById('match-phase-indicator')?.textContent || 'Pase en curso';
        const pauseProg = document.getElementById('pause-progress-text');
        if (pauseProg) pauseProg.textContent = phaseText;
        if (modalPause) modalPause.classList.add('open');
      });
    }

    if (btnResume) {
      btnResume.addEventListener('click', () => {
        if (modalPause) modalPause.classList.remove('open');
        state.match.isPaused = false;
        if (state.match.active && state.match.canAnswer) {
          startQuestionTimer(state.match.timeLeft);
        }
      });
    }

    if (btnRestart) {
      btnRestart.addEventListener('click', () => {
        if (modalPause) modalPause.classList.remove('open');
        state.match.isPaused = false;
        startSoloMatch();
      });
    }

    if (btnExitMenu) {
      btnExitMenu.addEventListener('click', () => {
        if (modalPause) modalPause.classList.remove('open');
        state.match.isPaused = false;
        endCurrentMatch();
        switchView('welcome');
      });
    }

    // Botón para saltar intro de inicio
    const btnSkipIntro = document.getElementById('btn-skip-intro');
    if (btnSkipIntro) {
      btnSkipIntro.addEventListener('click', () => {
        if (state.introTimeout) {
          clearTimeout(state.introTimeout);
          state.introTimeout = null;
        }
        triggerMatchStart();
      });
    }
  }

  // Entrada Cinemática del Partido con Logo de Fútbol Quiz
  function showMatchIntro(team1, team2, onStartCallback) {
    const overlay = document.getElementById('match-intro-overlay');
    if (!overlay) {
      onStartCallback();
      return;
    }

    // Actualizar datos del enfrentamiento
    document.getElementById('intro-p1-flag').textContent = team1.flag || '🇨🇴';
    document.getElementById('intro-p1-name').textContent = team1.name;
    document.getElementById('intro-p1-player').textContent = team1.player;

    document.getElementById('intro-p2-flag').textContent = team2.flag || '🇦🇷';
    document.getElementById('intro-p2-name').textContent = team2.name;
    document.getElementById('intro-p2-player').textContent = team2.player;

    overlay.classList.remove('hidden');
    window.sounds.playIntro();

    state.onIntroComplete = onStartCallback;
    state.introTimeout = setTimeout(() => {
      triggerMatchStart();
    }, 2800);
  }

  function triggerMatchStart() {
    const overlay = document.getElementById('match-intro-overlay');
    if (overlay) overlay.classList.add('hidden');
    window.sounds.playWhistle();
    if (state.onIntroComplete) {
      const cb = state.onIntroComplete;
      state.onIntroComplete = null;
      cb();
    }
  }

  // Generador de Banderas Circulares SVG para Fichas / Chapas (Estilo Soccer Stars)
  function getFlagSVG(teamCodeOrId) {
    const id = (teamCodeOrId || '').toLowerCase();
    if (id.includes('colombia') || id === 'co') {
      return `
        <svg viewBox="0 0 100 100" class="flag-disk-svg">
          <defs><clipPath id="clip-co"><circle cx="50" cy="50" r="48"/></clipPath></defs>
          <g clip-path="url(#clip-co)">
            <rect width="100" height="50" fill="#FCD116"/>
            <rect y="50" width="100" height="25" fill="#003893"/>
            <rect y="75" width="100" height="25" fill="#CE1126"/>
          </g>
        </svg>`;
    }
    if (id.includes('argentina') || id === 'ar') {
      return `
        <svg viewBox="0 0 100 100" class="flag-disk-svg">
          <defs><clipPath id="clip-ar"><circle cx="50" cy="50" r="48"/></clipPath></defs>
          <g clip-path="url(#clip-ar)">
            <rect width="100" height="33.3" fill="#75AADB"/>
            <rect y="33.3" width="100" height="33.4" fill="#FFFFFF"/>
            <rect y="66.7" width="100" height="33.3" fill="#75AADB"/>
            <circle cx="50" cy="50" r="9" fill="#F6B40E" stroke="#b45309" stroke-width="1"/>
            <circle cx="50" cy="50" r="4" fill="#d97706"/>
          </g>
        </svg>`;
    }
    if (id.includes('brasil') || id.includes('brazil') || id === 'br') {
      return `
        <svg viewBox="0 0 100 100" class="flag-disk-svg">
          <defs><clipPath id="clip-br"><circle cx="50" cy="50" r="48"/></clipPath></defs>
          <g clip-path="url(#clip-br)">
            <rect width="100" height="100" fill="#009739"/>
            <polygon points="50,14 90,50 50,86 10,50" fill="#FEDD00"/>
            <circle cx="50" cy="50" r="20" fill="#012169"/>
            <path d="M 32,53 Q 50,44 68,52" stroke="#FFFFFF" stroke-width="3" fill="none"/>
          </g>
        </svg>`;
    }
    if (id.includes('francia') || id.includes('france') || id === 'fr') {
      return `
        <svg viewBox="0 0 100 100" class="flag-disk-svg">
          <defs><clipPath id="clip-fr"><circle cx="50" cy="50" r="48"/></clipPath></defs>
          <g clip-path="url(#clip-fr)">
            <rect width="33.3" height="100" fill="#002395"/>
            <rect x="33.3" width="33.4" height="100" fill="#FFFFFF"/>
            <rect x="66.7" width="33.3" height="100" fill="#ED2939"/>
          </g>
        </svg>`;
    }
    if (id.includes('portugal') || id === 'pt') {
      return `
        <svg viewBox="0 0 100 100" class="flag-disk-svg">
          <defs><clipPath id="clip-pt"><circle cx="50" cy="50" r="48"/></clipPath></defs>
          <g clip-path="url(#clip-pt)">
            <rect width="40" height="100" fill="#046A38"/>
            <rect x="40" width="60" height="100" fill="#DA291C"/>
            <circle cx="40" cy="50" r="14" fill="#FFD700" stroke="#b45309" stroke-width="1"/>
            <circle cx="40" cy="50" r="8" fill="#DA291C"/>
          </g>
        </svg>`;
    }
    if (id.includes('alemania') || id.includes('germany') || id === 'de') {
      return `
        <svg viewBox="0 0 100 100" class="flag-disk-svg">
          <defs><clipPath id="clip-de"><circle cx="50" cy="50" r="48"/></clipPath></defs>
          <g clip-path="url(#clip-de)">
            <rect width="100" height="33.3" fill="#111111"/>
            <rect y="33.3" width="100" height="33.4" fill="#DD0000"/>
            <rect y="66.7" width="100" height="33.3" fill="#FFCE00"/>
          </g>
        </svg>`;
    }
    return `
      <svg viewBox="0 0 100 100" class="flag-disk-svg">
        <circle cx="50" cy="50" r="48" fill="#00e676"/>
        <text x="50" y="58" font-size="32" text-anchor="middle" fill="#032b14">⚽</text>
      </svg>`;
  }

  // Formación Táctica de 7 Jugadores por Equipo (7 Pases / Preguntas para Ganar)
  const PITCH_FORMATION_7 = {
    p1: [
      { id: 0, role: 'Portero', name: 'Arquero', num: 1, left: 8, top: 50 },
      { id: 1, role: 'Defensa Lateral', name: 'Defensa 1', num: 3, left: 21, top: 74 },
      { id: 2, role: 'Defensa Central', name: 'Defensa 2', num: 4, left: 21, top: 26 },
      { id: 3, role: 'Medio Defensivo', name: 'Contención', num: 6, left: 34, top: 50 },
      { id: 4, role: 'Volante Creativo', name: 'Organizador', num: 8, left: 49, top: 40 },
      { id: 5, role: 'Extremo Ofensivo', name: 'Extremo', num: 11, left: 63, top: 68 },
      { id: 6, role: 'Delantero Goleador', name: 'Goleador', num: 10, left: 78, top: 50 }
    ],
    p2: [
      { id: 0, role: 'Portero Rival', name: 'Arquero Rival', num: 1, left: 92, top: 50 },
      { id: 1, role: 'Defensa Rival 1', name: 'Defensa R1', num: 2, left: 80, top: 26 },
      { id: 2, role: 'Defensa Rival 2', name: 'Defensa R2', num: 5, left: 80, top: 74 },
      { id: 3, role: 'Medio Rival 1', name: 'Medio R1', num: 6, left: 66, top: 32 },
      { id: 4, role: 'Medio Rival 2', name: 'Medio R2', num: 8, left: 54, top: 62 },
      { id: 5, role: 'Medio Rival 3', name: 'Medio R3', num: 7, left: 40, top: 72 },
      { id: 6, role: 'Delantero Rival', name: 'Delantero Rival', num: 9, left: 28, top: 48 }
    ]
  };

  // Renderizar los 7 Jugadores de cada Selección con Banderas Circulares 3D
  function renderPitchPlayers() {
    const layer = document.getElementById('pitch-players-layer');
    if (!layer) return;
    layer.innerHTML = '';

    const t1 = state.match.team1;
    const t2 = state.match.team2;
    const t1FlagSVG = getFlagSVG(t1.name || state.selectedTeam?.id || 'colombia');
    const t2FlagSVG = getFlagSVG(t2.name || 'argentina');

    // 7 Jugadores Equipo 1 (Tú)
    PITCH_FORMATION_7.p1.forEach((p, idx) => {
      const el = document.createElement('div');
      el.className = 'field-player team-1';
      el.id = `fp-p1_${idx}`;
      el.style.left = `${p.left}%`;
      el.style.top = `${p.top}%`;

      const pName = idx === 6 ? (t1.player || p.name) : p.name;
      const pNum = idx === 6 ? (state.selectedPlayer?.number || p.num) : p.num;

      el.innerHTML = `
        <div class="player-token">
          ${t1FlagSVG}
          <span class="player-jersey-number">${pNum}</span>
        </div>
        <div class="player-name-tag">${pName}</div>
      `;
      layer.appendChild(el);
    });

    // 7 Jugadores Equipo 2 (Rival)
    PITCH_FORMATION_7.p2.forEach((p, idx) => {
      const el = document.createElement('div');
      el.className = 'field-player team-2';
      el.id = `fp-p2_${idx}`;
      el.style.left = `${p.left}%`;
      el.style.top = `${p.top}%`;

      const pName = idx === 6 ? (t2.player || p.name) : p.name;

      el.innerHTML = `
        <div class="player-token">
          ${t2FlagSVG}
          <span class="player-jersey-number">${p.num}</span>
        </div>
        <div class="player-name-tag">${pName}</div>
      `;
      layer.appendChild(el);
    });
  }

  // Dibujar Línea de Trayectoria Guiada (Matching User Reference Image)
  function drawPassTrajectory(currentPos) {
    const svg = document.getElementById('pitch-trajectory-svg');
    if (!svg) return;
    svg.innerHTML = '';

    const p1Players = PITCH_FORMATION_7.p1;
    const curr = p1Players[currentPos];
    let next = null;

    if (currentPos < 6) {
      next = p1Players[currentPos + 1];
    } else {
      next = { left: 96, top: 50 }; // Arco rival
    }

    if (curr && next) {
      const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', `${curr.left}%`);
      line.setAttribute('y1', `${curr.top}%`);
      line.setAttribute('x2', `${next.left}%`);
      line.setAttribute('y2', `${next.top}%`);
      line.setAttribute('class', 'pass-trajectory-line');
      svg.appendChild(line);
    }
  }

  // Actualizar Posición del Balón en Cancha entre los 7 Jugadores
  function updateBallPositionUI(position) {
    const ball = document.getElementById('match-ball');
    if (!ball) return;

    const safePos = Math.max(0, Math.min(6, position));
    const p1Players = PITCH_FORMATION_7.p1;
    const currentP = p1Players[safePos];

    // Posicionar balón a los pies del jugador activo
    ball.style.left = `calc(${currentP.left}% - 19px)`;
    ball.style.top = `calc(${currentP.top}% + 4px)`;
    ball.classList.add('pass-flight');
    setTimeout(() => ball.classList.remove('pass-flight'), 700);

    // Actualizar indicador de Pase (1 a 7)
    const phaseEl = document.getElementById('match-phase-indicator');
    if (phaseEl) {
      if (safePos === 6) {
        phaseEl.textContent = '⚡ Pase 7 de 7: ¡Tiro al Arco y Gol!';
      } else {
        phaseEl.textContent = `⚡ Pase ${safePos + 1} de 7: ${currentP.name}`;
      }
    }

    // Dibujar trayectoria
    drawPassTrajectory(safePos);
  }

  // Animar pases y dinámicas de personajes con Anillo Activo Naranja
  function updatePitchPlayersUI(ballPos, action = 'idle') {
    const players = document.querySelectorAll('.field-player');
    players.forEach(p => {
      p.classList.remove('active-possession', 'kicking', 'tackling', 'celebrating');
    });

    const isP1Turn = (state.match.turn === 'p1');
    const safePos = Math.max(0, Math.min(6, ballPos));

    let activeId = isP1Turn ? `fp-p1_${safePos}` : `fp-p2_${safePos}`;
    const carrier = document.getElementById(activeId);
    if (carrier) {
      carrier.classList.add('active-possession');
      if (action === 'kick') carrier.classList.add('kicking');
    }

    if (action === 'tackle') {
      const rivalId = `fp-p2_${safePos}`;
      const tackler = document.getElementById(rivalId);
      if (tackler) tackler.classList.add('tackling');
    }

    if (action === 'goal') {
      const scorer = document.getElementById('fp-p1_6');
      if (scorer) scorer.classList.add('celebrating');
    }
  }

  // Fisher-Yates Array Shuffler
  function shuffleArray(arr) {
    const res = [...arr];
    for (let i = res.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [res[i], res[j]] = [res[j], res[i]];
    }
    return res;
  }

  // Randomize options A, B, C, D so correct answer isn't predictable
  function randomizeOptions(q) {
    if (!q || !Array.isArray(q.opciones) || q.correcta === undefined) return q;
    const correctText = q.opciones[q.correcta];
    const indices = [0, 1, 2, 3].slice(0, q.opciones.length);
    const shuffledIndices = shuffleArray(indices);
    const newOptions = shuffledIndices.map(idx => q.opciones[idx]);
    const newCorrectIdx = newOptions.indexOf(correctText);
    return {
      ...q,
      opciones: newOptions,
      correcta: newCorrectIdx >= 0 ? newCorrectIdx : q.correcta
    };
  }

  // Anti-repetition session pool
  window._recentQuestionIds = window._recentQuestionIds || new Set();

  // Fetch Questions for Solo Match
  async function loadQuestionsForSolo() {
    let url = `/api/questions?grado=${state.selectedGrade}`;
    if (state.questionMode === 'subject') {
      url += `&asignatura=${encodeURIComponent(state.selectedSubject)}`;
    }
    try {
      const res = await fetch(url);
      let data = await res.json();
      if (!Array.isArray(data) || data.length === 0) {
        // Fallback: load all for grade
        const fallbackRes = await fetch(`/api/questions?grado=${state.selectedGrade}`);
        data = await fallbackRes.json();
      }
      if (!Array.isArray(data) || data.length === 0) {
        return [];
      }

      // Filter out recently seen questions to prevent repetition
      let unseen = data.filter(q => !window._recentQuestionIds.has(q.id));
      if (unseen.length < 7) {
        // Reset pool if running low on unseen questions
        window._recentQuestionIds.clear();
        unseen = data;
      }

      // Shuffle unseen questions with true Fisher-Yates
      const chosen = shuffleArray(unseen).slice(0, 15);

      // Track these IDs in recent memory
      chosen.forEach(q => window._recentQuestionIds.add(q.id));

      // Randomize the 4 options (A, B, C, D) for each question
      return chosen.map(q => randomizeOptions(q));
    } catch (err) {
      console.error('Error fetching questions:', err);
      return [];
    }
  }

  // Start Solo Match
  async function startSoloMatch() {
    state.isMultiplayer = false;
    const questions = await loadQuestionsForSolo();
    if (questions.length === 0) {
      alert('No se encontraron preguntas para este grado/asignatura. Selecciona otra opción.');
      return;
    }

    // Pick random rival team
    const rivals = state.teams.filter(t => t.id !== state.selectedTeam.id);
    const rivalTeam = rivals[Math.floor(Math.random() * rivals.length)] || state.teams[0];
    const rivalPlayer = rivalTeam.players[0];

    const team1Data = { name: state.selectedTeam.name, player: state.selectedPlayer.name, flag: state.selectedTeam.flag };
    const team2Data = { name: rivalTeam.name, player: rivalPlayer.name, flag: rivalTeam.flag };

    state.match = {
      active: true,
      ballPosition: 0, // Inicia en el Arquero (Jugador 1 de 7)
      scoreP1: 0,
      scoreP2: 0,
      academicPoints: 0,
      turn: 'p1',
      possession: 'p1',
      failedAttemptsInTurn: 0,
      questions,
      currentQuestionIndex: 0,
      currentQuestion: null,
      maxGoals: 1, // 7 pases/preguntas correctas para anotar y ganar
      timerSec: 60, // Límite de 1 minuto por pregunta
      timerId: null,
      timeLeft: 60,
      isPaused: false,
      canAnswer: false,
      team1: team1Data,
      team2: team2Data,
      stats: { total: 0, correct: 0, wrong: 0, subjects: {} }
    };

    // Asegurar que el botón de pausa esté visible en modo offline/solo
    const btnPause = document.getElementById('btn-pause-match');
    if (btnPause) btnPause.style.display = 'inline-flex';

    // Lanzar Entrada Cinemática con Logo de Fútbol Quiz
    showMatchIntro(team1Data, team2Data, () => {
      updateScoreboardUI();
      renderPitchPlayers();
      updateBallPositionUI(0);
      updatePitchPlayersUI(0, 'idle');
      switchView('match');
      showPlayAlert('⚡ ¡Inicia el partido! Responde 7 preguntas (7 pases entre tus 7 jugadores) para marcar el gol de la victoria.', 'turn');
      loadNextSoloQuestion();
    });
  }

  function updateScoreboardUI() {
    document.getElementById('scoreboard-team1-name').textContent = state.match.team1.name;
    document.getElementById('scoreboard-player1-name').textContent = `${state.match.team1.player} (Tú)`;
    document.getElementById('score-p1').textContent = state.match.scoreP1;

    document.getElementById('scoreboard-team2-name').textContent = state.match.team2.name;
    document.getElementById('scoreboard-player2-name').textContent = `${state.match.team2.player} (Rival)`;
    document.getElementById('score-p2').textContent = state.match.scoreP2;

    const badge = document.getElementById('match-possession-badge');
    if (state.match.turn === 'p1') {
      badge.textContent = 'TU POSESIÓN';
      badge.style.borderColor = 'var(--accent-green)';
      badge.style.color = 'var(--accent-green)';
    } else {
      badge.textContent = 'POSESIÓN RIVAL';
      badge.style.borderColor = 'var(--warning-amber)';
      badge.style.color = 'var(--warning-amber)';
    }
  }

  function showPlayAlert(msg, type = 'turn') {
    const banner = document.getElementById('play-alert-banner');
    const text = document.getElementById('play-alert-text');
    const icon = document.getElementById('play-alert-icon');

    banner.className = 'play-alert-banner';
    if (type === 'goal') {
      banner.classList.add('alert-goal');
      icon.textContent = '⚽🔥';
    } else if (type === 'warning') {
      banner.classList.add('alert-warning');
      icon.textContent = '⚠️';
    } else {
      banner.classList.add('alert-turn');
      icon.textContent = '⚡';
    }

    text.textContent = msg;
  }

  // Cálculo dinámico del tiempo según la dificultad y complejidad de la pregunta
  function getQuestionTimeLimit(q) {
    if (!q) return 60;
    if (typeof q.tiempoLimite === 'number') return q.tiempoLimite;

    const diff = (q.dificultad || '').toLowerCase();
    let baseTime = 60; // Normal / Medio

    if (diff.includes('difícil') || diff.includes('dificil') || diff.includes('avanzad')) {
      baseTime = 95; // Pregunta difícil: tiempo necesario para pensar y resolver (1m 35s)
    } else if (diff.includes('fácil') || diff.includes('facil')) {
      baseTime = 45; // Pregunta fácil: ágil pero holgado (45s)
    } else {
      baseTime = 65; // Pregunta normal: equilibrada (1m 05s)
    }

    // Bonificación si el enunciado es extenso o requiere cálculos matemáticos
    const textLen = (q.pregunta || '').length;
    if (textLen > 220) {
      baseTime += 15;
    } else if (textLen > 140) {
      baseTime += 10;
    }

    if (q.asignatura === 'Matemáticas' && baseTime < 80 && (diff.includes('medio') || diff.includes('dif'))) {
      baseTime = Math.max(baseTime, 85);
    }

    return Math.min(120, Math.max(40, baseTime));
  }

  function loadNextSoloQuestion() {
    clearInterval(state.match.timerId);
    const explanationBox = document.getElementById('match-explanation-box');
    explanationBox.style.display = 'none';

    // Reset buttons
    const btns = document.querySelectorAll('.answer-option-btn');
    btns.forEach(b => {
      b.className = 'answer-option-btn';
      b.disabled = false;
    });

    const q = state.match.questions[state.match.currentQuestionIndex];
    state.match.currentQuestion = q;

    // Render Question
    document.getElementById('badge-question-grade').textContent = `${q.grado}.º Grado`;
    document.getElementById('badge-question-subject').textContent = q.asignatura;
    document.getElementById('badge-question-diff').textContent = q.dificultad || 'Normal';
    document.getElementById('match-question-text').textContent = q.pregunta;

    btns.forEach(btn => {
      const idx = parseInt(btn.dataset.index, 10);
      const textSpan = btn.querySelector('.answer-text');
      textSpan.textContent = q.opciones[idx] || '';
    });

    updateScoreboardUI();
    updatePitchPlayersUI(state.match.ballPosition, 'idle');

    state.match.turn = 'p1';
    state.match.canAnswer = true;
    
    // Iniciar temporizador con duración adaptativa según dificultad
    const timeForQ = getQuestionTimeLimit(q);
    state.match.timerSec = timeForQ;
    startQuestionTimer(timeForQ);
  }

  // Temporizador dinámico con soporte de pausa
  function startQuestionTimer(customSec) {
    clearInterval(state.match.timerId);
    const maxSec = (typeof customSec === 'number') ? customSec : (state.match.timerSec || 60);
    state.match.timerSec = maxSec;
    let timeLeft = maxSec;
    state.match.timeLeft = timeLeft;
    const timeDisplay = document.getElementById('match-timer-display');
    const badgeTime = document.getElementById('badge-question-time');
    const timerBar = document.getElementById('match-timer-bar');

    timeDisplay.textContent = `${timeLeft}s`;
    badgeTime.textContent = `⏱️ ${timeLeft}s`;
    if (timerBar) {
      timerBar.style.width = '100%';
      timerBar.className = 'timer-progress-bar';
    }

    state.match.timerId = setInterval(() => {
      if (state.match.isPaused) return;
      timeLeft--;
      state.match.timeLeft = timeLeft;
      timeDisplay.textContent = `${timeLeft}s`;
      badgeTime.textContent = `⏱️ ${timeLeft}s`;

      if (timerBar) {
        const pct = Math.max(0, (timeLeft / state.match.timerSec) * 100);
        timerBar.style.width = `${pct}%`;
        if (timeLeft <= 15) {
          timerBar.className = 'timer-progress-bar danger';
        } else if (timeLeft <= 30) {
          timerBar.className = 'timer-progress-bar warning';
        } else {
          timerBar.className = 'timer-progress-bar';
        }
      }

      if (timeLeft <= 0) {
        clearInterval(state.match.timerId);
        submitAnswer(-1);
      }
    }, 1000);
  }

  // Answer Submitted by Player
  function submitAnswer(selectedIndex) {
    if (!state.match.canAnswer) return;
    state.match.canAnswer = false;
    clearInterval(state.match.timerId);

    const q = state.match.currentQuestion;
    const isCorrect = selectedIndex === q.correcta;

    // Highlight options
    const btns = document.querySelectorAll('.answer-option-btn');
    btns.forEach(btn => {
      const idx = parseInt(btn.dataset.index, 10);
      btn.disabled = true;
      if (idx === q.correcta) {
        btn.classList.add('correct');
      } else if (idx === selectedIndex) {
        btn.classList.add('wrong');
      }
    });

    // Show academic explanation
    const expBox = document.getElementById('match-explanation-box');
    const expText = document.getElementById('match-explanation-text');
    expText.textContent = q.explicacion;
    expBox.style.display = 'block';

    // Track stats
    state.match.stats.total++;
    state.match.stats.subjects[q.asignatura] = state.match.stats.subjects[q.asignatura] || { correct: 0, total: 0 };
    state.match.stats.subjects[q.asignatura].total++;

    if (isCorrect) {
      window.sounds.playCorrect();
      window.sounds.playPass();
      showAnswerFeedback(true, '¡RESPUESTA CORRECTA!', '¡Pase perfecto al compañero! (+100 Pts)');
      state.match.stats.correct++;
      state.match.stats.subjects[q.asignatura].correct++;
      state.match.academicPoints += 100;

      // Animación de pase entre personajes
      updatePitchPlayersUI(state.match.ballPosition, 'kick');

      // Avanzar al siguiente jugador de los 7 (posiciones 0 a 6)
      state.match.ballPosition++;

      if (state.match.ballPosition >= 7) {
        // Se completaron los 7 pases con los 7 jugadores -> Tiro al arco y ¡GOLAZO!
        updateBallPositionUI(6);
        updatePitchPlayersUI(6, 'goal');
        handleGoalScored('p1');
        return;
      } else {
        updateBallPositionUI(state.match.ballPosition);
        showPlayAlert(`¡Pase ${state.match.ballPosition} de 7 completado! Balón en pies del compañero ⚽`, 'turn');
      }
      state.match.failedAttemptsInTurn = 0;
      state.match.turn = 'p1';

    } else {
      window.sounds.playWrong();
      showAnswerFeedback(false, '¡PASE INTERCEPTADO!', 'Revisa la explicación pedagógica');
      state.match.stats.wrong++;

      // Animación de barrida / pérdida del balón
      updatePitchPlayersUI(state.match.ballPosition, 'tackle');

      // El balón retrocede una posición para que el usuario recupere el pase
      state.match.ballPosition = Math.max(0, state.match.ballPosition - 1);
      updateBallPositionUI(state.match.ballPosition);
      showPlayAlert('¡Pase interceptado! El balón retrocede una posición. ¡Concéntrate para el próximo pase! ⚠️', 'warning');
      state.match.turn = 'p1';
    }

    advanceMatchAfterRound();
  }

  // CPU Rival Simulation (Solo Mode)
  function simulateCpuTurn() {
    const q = state.match.currentQuestion;
    // 65% probability CPU answers correctly
    const isCpuCorrect = Math.random() < 0.65;
    const cpuAnswerIndex = isCpuCorrect ? q.correcta : (q.correcta + 1) % 4;

    const btns = document.querySelectorAll('.answer-option-btn');
    btns.forEach(btn => {
      const idx = parseInt(btn.dataset.index, 10);
      if (idx === q.correcta) {
        btn.classList.add('correct');
      } else if (idx === cpuAnswerIndex && !isCpuCorrect) {
        btn.classList.add('wrong');
      }
    });

    const expBox = document.getElementById('match-explanation-box');
    const expText = document.getElementById('match-explanation-text');
    expText.textContent = q.explicacion;
    expBox.style.display = 'block';

    if (isCpuCorrect) {
      window.sounds.playPass();
      updatePitchPlayersUI(state.match.ballPosition, 'kick');

      // CPU attacks towards Position 0
      state.match.ballPosition--;
      updateBallPositionUI(state.match.ballPosition);

      if (state.match.ballPosition <= 0) {
        updatePitchPlayersUI(state.match.ballPosition, 'goal');
        handleGoalScored('p2');
        return;
      } else {
        showPlayAlert(`¡El rival realiza un pase filtrado hacia tu arco! ⚽`, 'warning');
      }
      state.match.turn = 'p2';
      state.match.failedAttemptsInTurn = 0;

    } else {
      window.sounds.playWrong();
      updatePitchPlayersUI(state.match.ballPosition, 'tackle');

      if (state.match.failedAttemptsInTurn === 1) {
        showPlayAlert('¡El rival perdió el control del balón! ¡Recuperas la posesión! 🛡️', 'turn');
        state.match.turn = 'p1';
        state.match.failedAttemptsInTurn = 2;
      } else {
        showPlayAlert('¡El rival erró el pase! Es tu oportunidad para contraatacar ⚡', 'turn');
        state.match.turn = 'p1';
        state.match.failedAttemptsInTurn = 1;
      }
    }

    advanceMatchAfterRound();
  }

  function handleGoalScored(scorer) {
    window.sounds.playGoal();
    if (scorer === 'p1') {
      state.match.scoreP1++;
      showPlayAlert(`¡¡¡GOOOOOOOLAZO DE ${state.match.team1.name.toUpperCase()}!!! ⚽🔥`, 'goal');
    } else {
      state.match.scoreP2++;
      showPlayAlert(`¡GOL DE ${state.match.team2.name.toUpperCase()}! ⚽`, 'goal');
    }

    updateScoreboardUI();
    state.match.ballPosition = 3;
    setTimeout(() => updateBallPositionUI(3), 600);

    // Check Match Win
    if (state.match.scoreP1 >= state.match.maxGoals || state.match.scoreP2 >= state.match.maxGoals) {
      setTimeout(showFinalResults, 2800);
      return;
    }

    // Possession resets after goal to conceding team
    state.match.turn = scorer === 'p1' ? 'p2' : 'p1';
    state.match.failedAttemptsInTurn = 0;

    advanceMatchAfterRound(3000);
  }

  function showAnswerFeedback(isCorrect, headline, subtitle) {
    const popup = document.getElementById('answer-feedback-popup');
    if (!popup) return;
    const icon = document.getElementById('feedback-ball-icon');
    const title = document.getElementById('feedback-title');
    const sub = document.getElementById('feedback-subtitle');

    if (isCorrect) {
      popup.className = 'answer-feedback-popup';
      if (icon) icon.textContent = '⚽✨';
      if (title) title.textContent = headline || '¡RESPUESTA CORRECTA!';
      if (sub) sub.textContent = subtitle || '+100 PUNTOS DE SABER';
    } else {
      popup.className = 'answer-feedback-popup wrong-feedback';
      if (icon) icon.textContent = '❌⚽';
      if (title) title.textContent = headline || '¡PASE INTERCEPTADO!';
      if (sub) sub.textContent = subtitle || 'Revisa la explicación pedagógica';
    }

    popup.classList.remove('hidden');
    setTimeout(() => {
      popup.classList.add('hidden');
    }, 2000);
  }

  function advanceMatchAfterRound(delay = 2400) {
    setTimeout(() => {
      state.match.currentQuestionIndex = (state.match.currentQuestionIndex + 1) % state.match.questions.length;
      loadNextSoloQuestion();
    }, delay);
  }

  // --- MULTIPLAYER CLIENT MATCH HANDLING ---
  function startMultiMatchClient(data) {
    state.isMultiplayer = true;
    state.match.active = true;
    state.match.maxGoals = data.room.settings.maxGoals;
    state.match.timerSec = 60; // 1 minuto

    // En multijugador online no se puede pausar, solo cancelar
    const btnPause = document.getElementById('btn-pause-match');
    if (btnPause) btnPause.style.display = 'none';

    state.match.team1 = {
      name: data.room.players.host.team.name,
      player: data.room.players.host.name,
      flag: data.room.players.host.team.flag || '🇨🇴'
    };
    state.match.team2 = {
      name: data.room.players.guest.team.name,
      player: data.room.players.guest.name,
      flag: data.room.players.guest.team.flag || '🇦🇷'
    };

    showMatchIntro(state.match.team1, state.match.team2, () => {
      updateScoreboardUI();
      renderPitchPlayers();
      updateBallPositionUI(3);
      updatePitchPlayersUI(3, 'idle');
      switchView('match');
      renderMultiQuestion(data.currentQuestion, data.room.matchState.turn);
    });
  }

  function renderMultiQuestion(q, turn) {
    clearInterval(state.match.timerId);
    document.getElementById('match-explanation-box').style.display = 'none';

    const btns = document.querySelectorAll('.answer-option-btn');
    btns.forEach(b => {
      b.className = 'answer-option-btn';
      b.disabled = false;
    });

    state.match.currentQuestion = q;
    document.getElementById('badge-question-grade').textContent = `${q.grado}.º Grado`;
    document.getElementById('badge-question-subject').textContent = q.asignatura;
    document.getElementById('badge-question-diff').textContent = q.dificultad || 'Fácil';
    document.getElementById('match-question-text').textContent = q.pregunta;

    btns.forEach(btn => {
      const idx = parseInt(btn.dataset.index, 10);
      btn.querySelector('.answer-text').textContent = q.opciones[idx] || '';
    });

    state.match.turn = turn;
    const isMyTurn = (state.myRole === turn);
    state.match.canAnswer = isMyTurn;

    updateScoreboardUI();
    updatePitchPlayersUI(state.match.ballPosition, 'idle');

    const badge = document.getElementById('match-possession-badge');
    badge.textContent = isMyTurn ? 'TU TURNO DE RESPONDER' : 'TURNO DEL RIVAL';
    badge.style.color = isMyTurn ? 'var(--accent-green)' : 'var(--warning-amber)';

    if (isMyTurn) {
      showPlayAlert('¡Es tu turno! Responde para realizar el pase y avanzar ⚽', 'turn');
      const timeForQ = q.tiempoLimite || getQuestionTimeLimit(q);
      startQuestionTimer(timeForQ);
    } else {
      showPlayAlert('El contrincante está respondiendo la pregunta...', 'warning');
      document.getElementById('badge-question-time').textContent = 'Esperando rival...';
      const timerBar = document.getElementById('match-timer-bar');
      if (timerBar) timerBar.style.width = '100%';
    }
  }

  function handleMultiRoundResult(data) {
    clearInterval(state.match.timerId);

    // Show answers on buttons
    const btns = document.querySelectorAll('.answer-option-btn');
    btns.forEach(btn => {
      const idx = parseInt(btn.dataset.index, 10);
      btn.disabled = true;
      if (idx === data.correctAnswer) btn.classList.add('correct');
      if (idx === data.selectedAnswer && !data.isCorrect) btn.classList.add('wrong');
    });

    // Show explanation
    document.getElementById('match-explanation-box').style.display = 'block';
    document.getElementById('match-explanation-text').textContent = data.explanation;

    // Update ball, players animation & scores
    updateBallPositionUI(data.ballPosition);
    state.match.ballPosition = data.ballPosition;
    state.match.scoreP1 = data.scores.host;
    state.match.scoreP2 = data.scores.guest;
    updateScoreboardUI();

    if (data.isCorrect) {
      window.sounds.playCorrect();
      window.sounds.playPass();
      showAnswerFeedback(true, '¡RESPUESTA CORRECTA!', '¡Pase perfecto al compañero! (+100 Pts)');
      updatePitchPlayersUI(data.ballPosition, 'kick');
    } else {
      window.sounds.playWrong();
      showAnswerFeedback(false, '¡PASE INTERCEPTADO!', 'Revisa la explicación pedagógica');
      updatePitchPlayersUI(data.ballPosition, 'tackle');
    }

    if (data.goalScoredBy) {
      window.sounds.playGoal();
      updatePitchPlayersUI(data.ballPosition, 'goal');
      showPlayAlert(`¡¡¡GOOOOOOOLAZO!!! ⚽🔥`, 'goal');
    }

    if (data.matchWinner) {
      setTimeout(() => {
        showFinalResults(data.matchWinner === state.myRole);
      }, 3000);
      return;
    }

    setTimeout(() => {
      renderMultiQuestion(data.nextQuestion, data.nextTurn);
    }, 2800);
  }

  // --- 8. RESULTS VIEW ---
  function showFinalResults(isWinner) {
    clearInterval(state.match.timerId);
    state.match.active = false;
    window.sounds.playWhistle();

    const p1Score = state.match.scoreP1;
    const p2Score = state.match.scoreP2;
    const won = isWinner !== undefined ? isWinner : (p1Score > p2Score);

    const winnerTitle = document.getElementById('results-winner-title');
    const subtitle = document.getElementById('results-subtitle');

    if (won) {
      winnerTitle.textContent = `¡${state.match.team1.name.toUpperCase()} CAMPEÓN! 🏆`;
      subtitle.textContent = '¡Felicitaciones! Has conquistado La Copa del Saber con tu talento académico.';
    } else if (p1Score === p2Score) {
      winnerTitle.textContent = '¡EMPATE HISTÓRICO! 🤝';
      subtitle.textContent = 'Ambos equipos demostraron un nivel académico sobresaliente en la cancha.';
    } else {
      winnerTitle.textContent = `¡GANADOR: ${state.match.team2.name.toUpperCase()}! ⚽`;
      subtitle.textContent = 'Gran esfuerzo. Prepárate y busca la revancha en el próximo partido.';
    }

    document.getElementById('res-stat-score').textContent = `${p1Score} - ${p2Score}`;
    document.getElementById('res-stat-points').textContent = state.match.academicPoints;

    const total = state.match.stats.total || 1;
    const correct = state.match.stats.correct || 0;
    const accPct = Math.round((correct / total) * 100);
    document.getElementById('res-stat-accuracy').textContent = `${accPct}%`;
    document.getElementById('res-stat-questions').textContent = state.match.stats.total;

    // Pedagogical Feedback
    let feedback = `Has obtenido una efectividad del ${accPct}% en esta prueba. `;
    if (accPct >= 80) {
      feedback += '¡Excelente dominio de las competencias evaluadas en las pruebas ICFES! Sigue manteniendo tu ritmo.';
    } else if (accPct >= 50) {
      feedback += 'Buen desempeño general. Te recomendamos reforzar la lectura de los enunciados y análisis de opciones.';
    } else {
      feedback += 'Recuerda revisar las explicaciones de cada pregunta para fortalecer los conceptos clave de tu grado.';
    }
    document.getElementById('res-feedback-text').textContent = feedback;

    switchView('results');
  }

  function setupResultsView() {
    document.getElementById('btn-play-again').addEventListener('click', () => {
      window.sounds.playKick();
      if (state.gameMode === 'solo') {
        startSoloMatch();
      } else {
        openMultiplayerLobby();
      }
    });

    document.getElementById('btn-back-home').addEventListener('click', () => {
      endCurrentMatch();
      switchView('welcome');
    });
  }

  function endCurrentMatch() {
    clearInterval(state.match.timerId);
    state.match.active = false;
    if (state.socket) {
      state.socket.disconnect();
      state.socket = null;
    }
  }

  // Run on page load
  window.addEventListener('DOMContentLoaded', init);

})();
