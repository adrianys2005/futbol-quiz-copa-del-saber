# -*- coding: utf-8 -*-
"""
Enrich data/questions.json with easy, snappy, direct Grade 11 questions
for all 5 ICFES subjects: Matemáticas, Lenguaje, Ciencias Naturales, Ciencias Sociales, Inglés.
"""
import json

easy_questions = [
  # --- MATEMÁTICAS (FÁCILES - GRADO 11) ---
  {
    "id": "MAT-11-FAC-01",
    "grado": "11",
    "asignatura": "Matemáticas",
    "tema": "Porcentajes y descuentos",
    "pregunta": "Un balón oficial cuesta $100.000 y tiene un descuento del 20%. ¿Cuánto pagará el comprador por el balón?",
    "opciones": ["$ 20.000", "$ 70.000", "$ 80.000", "$ 90.000"],
    "correcta": 2,
    "explicacion": "El 20% de 100.000 es 20.000. Restando el descuento: 100.000 - 20.000 = $80.000.",
    "dificultad": "Fácil",
    "fuente": "Fundamentos Saber 11° Matemáticas"
  },
  {
    "id": "MAT-11-FAC-02",
    "grado": "11",
    "asignatura": "Matemáticas",
    "tema": "Áreas y geometría básica",
    "pregunta": "¿Cuál es el área de una cancha rectangular que mide 10 metros de ancho por 20 metros de largo?",
    "opciones": ["30 m²", "60 m²", "200 m²", "400 m²"],
    "correcta": 2,
    "explicacion": "El área de un rectángulo es base × altura: 20 m × 10 m = 200 m².",
    "dificultad": "Fácil",
    "fuente": "Fundamentos Saber 11° Matemáticas"
  },
  {
    "id": "MAT-11-FAC-03",
    "grado": "11",
    "asignatura": "Matemáticas",
    "tema": "Probabilidad simple",
    "pregunta": "Al lanzar una moneda al aire antes de iniciar el partido, ¿cuál es la probabilidad de que caiga cara?",
    "opciones": ["1/4 (25%)", "1/2 (50%)", "1/3 (33%)", "1/1 (100%)"],
    "correcta": 1,
    "explicacion": "Hay 1 caso favorable (cara) entre 2 casos posibles (cara o sello), por tanto es 1/2 = 50%.",
    "dificultad": "Fácil",
    "fuente": "Fundamentos Saber 11° Matemáticas"
  },
  {
    "id": "MAT-11-FAC-04",
    "grado": "11",
    "asignatura": "Matemáticas",
    "tema": "Operaciones con fracciones",
    "pregunta": "En un partido se han jugado 45 minutos de los 90 reglamentarios. ¿Qué fracción del tiempo total se ha jugado?",
    "opciones": ["1/4", "1/3", "1/2", "3/4"],
    "correcta": 2,
    "explicacion": "45 / 90 = 1/2, es decir exactamente la mitad del partido.",
    "dificultad": "Fácil",
    "fuente": "Fundamentos Saber 11° Matemáticas"
  },
  {
    "id": "MAT-11-FAC-05",
    "grado": "11",
    "asignatura": "Matemáticas",
    "tema": "Promedios simples",
    "pregunta": "Un delantero anotó 2 goles en el primer partido, 4 en el segundo y 0 en el tercero. ¿Cuál es su promedio de goles por partido?",
    "opciones": ["1 gol", "2 goles", "3 goles", "6 goles"],
    "correcta": 1,
    "explicacion": "Promedio = (2 + 4 + 0) ÷ 3 = 6 ÷ 3 = 2 goles por partido.",
    "dificultad": "Fácil",
    "fuente": "Fundamentos Saber 11° Matemáticas"
  },

  # --- LENGUAJE / LECTURA CRÍTICA (FÁCILES - GRADO 11) ---
  {
    "id": "LEN-11-FAC-01",
    "grado": "11",
    "asignatura": "Lenguaje",
    "tema": "Sinónimos contextuales",
    "pregunta": "En la frase: 'El guardameta tuvo una actuación formidable durante la final', la palabra 'formidable' puede sustituirse sin cambiar el sentido por:",
    "opciones": ["Pésima", "Grandiosa", "Común", "Peligrosa"],
    "correcta": 1,
    "explicacion": "'Formidable' en este contexto significa magnífica, excelente o grandiosa.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Lectura Crítica"
  },
  {
    "id": "LEN-11-FAC-02",
    "grado": "11",
    "asignatura": "Lenguaje",
    "tema": "Conectores lógicos de causa",
    "pregunta": "¿Cuál de los siguientes conectores indica la causa de un hecho?",
    "opciones": ["Sin embargo", "Porque", "Por el contrario", "Finalmente"],
    "correcta": 1,
    "explicacion": "'Porque' es una conjunción causal que introduce la razón o motivo de una acción.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Lectura Crítica"
  },
  {
    "id": "LEN-11-FAC-03",
    "grado": "11",
    "asignatura": "Lenguaje",
    "tema": "Tipología textual",
    "pregunta": "Un texto que expone opiniones fundamentadas para convencer al lector sobre una tesis se clasifica como:",
    "opciones": ["Instructivo", "Descriptivo", "Argumentativo", "Lírico"],
    "correcta": 2,
    "explicacion": "El texto argumentativo tiene como propósito principal convencer o persuadir al receptor mediante argumentos razonados.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Lectura Crítica"
  },
  {
    "id": "LEN-11-FAC-04",
    "grado": "11",
    "asignatura": "Lenguaje",
    "tema": "Intención comunicativa",
    "pregunta": "Un afiche que dice: '¡Usa el cinturón de seguridad, salva tu vida!', tiene como función principal:",
    "opciones": ["Contar una historia de ficción", "Persuadir y prevenir al ciudadano", "Entretener con humor", "Explicar una fórmula matemática"],
    "correcta": 1,
    "explicacion": "Los afiches de seguridad vial buscan persuadir y concientizar a la población para prevenir accidentes.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Lectura Crítica"
  },

  # --- CIENCIAS NATURALES (FÁCILES - GRADO 11) ---
  {
    "id": "CN-11-FAC-01",
    "grado": "11",
    "asignatura": "Ciencias Naturales",
    "tema": "Física - Movimiento y velocidad",
    "pregunta": "Si un jugador corre 100 metros en 10 segundos con velocidad constante, ¿cuál es su rapidez?",
    "opciones": ["5 m/s", "10 m/s", "50 m/s", "100 m/s"],
    "correcta": 1,
    "explicacion": "Rapidez = Distancia ÷ Tiempo = 100 m ÷ 10 s = 10 m/s.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Ciencias Naturales"
  },
  {
    "id": "CN-11-FAC-02",
    "grado": "11",
    "asignatura": "Ciencias Naturales",
    "tema": "Biología - Fotosíntesis",
    "pregunta": "¿Cuál es el principal gas que absorben las plantas de la atmósfera para realizar la fotosíntesis?",
    "opciones": ["Oxígeno (O₂)", "Dióxido de carbono (CO₂)", "Nitrógeno (N₂)", "Monóxido de carbono (CO)"],
    "correcta": 1,
    "explicacion": "Las plantas toman dióxido de carbono (CO₂) y agua en presencia de luz solar para producir glucosa y liberar oxígeno.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Ciencias Naturales"
  },
  {
    "id": "CN-11-FAC-03",
    "grado": "11",
    "asignatura": "Ciencias Naturales",
    "tema": "Química - Estados de la materia",
    "pregunta": "El paso directo del estado líquido al gaseoso debido al aumento de temperatura se conoce como:",
    "opciones": ["Condensación", "Solidificación", "Evaporación / Ebullición", "Sublimación"],
    "correcta": 2,
    "explicacion": "La evaporación o ebullición es el cambio físico de líquido a gas.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Ciencias Naturales"
  },
  {
    "id": "CN-11-FAC-04",
    "grado": "11",
    "asignatura": "Ciencias Naturales",
    "tema": "Física - Conservación de la energía",
    "pregunta": "¿Qué establece el principio fundamental de conservación de la energía?",
    "opciones": [
      "La energía se crea espontáneamente de la nada.",
      "La energía no se crea ni se destruye, solo se transforma.",
      "La energía siempre desaparece al final de un movimiento.",
      "La energía potencial nunca puede convertirse en energía cinética."
    ],
    "correcta": 1,
    "explicacion": "La Primera Ley de la Termodinámica afirma que la energía total de un sistema aislado permanece constante: no se crea ni se destruye, solo cambia de forma.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Ciencias Naturales"
  },

  # --- CIENCIAS SOCIALES (FÁCILES - GRADO 11) ---
  {
    "id": "SOC-11-FAC-01",
    "grado": "11",
    "asignatura": "Ciencias Sociales",
    "tema": "Constitución de 1991 y Derechos",
    "pregunta": "En Colombia, ¿cuál es el mecanismo constitucional creado en 1991 que protege de forma rápida los derechos fundamentales de las personas?",
    "opciones": ["La acción de tutela", "El referendo", "El juicio político", "La moción de censura"],
    "correcta": 0,
    "explicacion": "La Acción de Tutela (Artículo 86 de la Constitución de 1991) permite a cualquier ciudadano solicitar la protección inmediata de sus derechos fundamentales ante los jueces.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Competencias Ciudadanas"
  },
  {
    "id": "SOC-11-FAC-02",
    "grado": "11",
    "asignatura": "Ciencias Sociales",
    "tema": "Ramas del Poder Público",
    "pregunta": "¿Qué rama del poder público en Colombia se encarga de crear y reformar las leyes a través del Congreso de la República?",
    "opciones": ["Rama Ejecutiva", "Rama Legislativa", "Rama Judicial", "Rama Electoral"],
    "correcta": 1,
    "explicacion": "La Rama Legislativa está conformada por el Congreso (Senado y Cámara de Representantes) y tiene la función de legislar.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Ciencias Sociales"
  },
  {
    "id": "SOC-11-FAC-03",
    "grado": "11",
    "asignatura": "Ciencias Sociales",
    "tema": "Mecanismos de participación",
    "pregunta": "El mecanismo mediante el cual el pueblo vota para elegir al Presidente, alcaldes o concejales se denomina:",
    "opciones": ["El sufragio / Voto popular", "El cabildo abierto", "La huelga", "La revocatoria"],
    "correcta": 0,
    "explicacion": "El voto o sufragio universal es el derecho y deber ciudadano fundamental para elegir a los gobernantes en una democracia.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Ciencias Sociales"
  },
  {
    "id": "SOC-11-FAC-04",
    "grado": "11",
    "asignatura": "Ciencias Sociales",
    "tema": "Geografía de Colombia",
    "pregunta": "¿Por cuántos océanos está rodeado el territorio de la República de Colombia?",
    "opciones": ["Ninguno (es país mediterráneo)", "Uno solo (Océano Atlántico)", "Dos océanos (Atlántico y Pacífico)", "Tres océanos"],
    "correcta": 2,
    "explicacion": "Colombia es el único país de Sudamérica con costas en dos océanos: el Mar Caribe (Océano Atlántico) y el Océano Pacífico.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Ciencias Sociales"
  },

  # --- INGLÉS (FÁCILES - GRADO 11) ---
  {
    "id": "ING-11-FAC-01",
    "grado": "11",
    "asignatura": "Inglés",
    "tema": "Everyday greetings and polite responses",
    "pregunta": "Complete the conversation: - 'Good luck in today's soccer match!' - '_________________'",
    "opciones": ["You are welcome", "Thanks, I will do my best!", "I'm 17 years old", "It is raining outside"],
    "correcta": 1,
    "explicacion": "The natural response when wished good luck is 'Thanks, I will do my best!'",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Inglés"
  },
  {
    "id": "ING-11-FAC-02",
    "grado": "11",
    "asignatura": "Inglés",
    "tema": "Prepositions of place",
    "pregunta": "Where is the soccer ball? 'The ball is _______ the grass in the center of the field.'",
    "opciones": ["on", "under", "between", "behind"],
    "correcta": 0,
    "explicacion": "'On' is used for objects resting on a surface like 'on the grass'.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Inglés"
  },
  {
    "id": "ING-11-FAC-03",
    "grado": "11",
    "asignatura": "Inglés",
    "tema": "Sports and school vocabulary",
    "pregunta": "Which word corresponds to the person who protects the goal in a soccer match?",
    "opciones": ["Referee", "Goalkeeper", "Coach", "Fan"],
    "correcta": 1,
    "explicacion": "The 'goalkeeper' (portero / arquero) is the player whose role is preventing the ball from entering the goal.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Inglés"
  },
  {
    "id": "ING-11-FAC-04",
    "grado": "11",
    "asignatura": "Inglés",
    "tema": "Present Simple vs Past",
    "pregunta": "Choose the correct past form: 'Yesterday, our team _______ the championship match 3 to 1.'",
    "opciones": ["win", "won", "winning", "wins"],
    "correcta": 1,
    "explicacion": "The past simple of the irregular verb 'win' is 'won'.",
    "dificultad": "Fácil",
    "fuente": "Saber 11° Inglés"
  }
]

# Load existing ICFES questions and prepend the easy questions so they are picked first!
try:
    with open('data/questions.json', 'r', encoding='utf-8') as f:
        existing = json.load(f)
except Exception:
    existing = []

all_q = easy_questions + existing
print(f"Total compiled questions: {len(all_q)} ({len(easy_questions)} easy questions added)")

with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_q, f, ensure_ascii=False, indent=2)

print("Saved to data/questions.json successfully!")
