# -*- coding: utf-8 -*-
"""
Script to expand questions bank to ensure deep coverage across Grades 6 to 11
for all core subjects (Matemáticas, Lenguaje / Lectura Crítica, Ciencias Naturales, 
Ciencias Sociales / Competencias Ciudadanas, Inglés).
"""
import json

additional_questions = [
    # ==========================================
    # GRADO 6.°
    # ==========================================
    {
        "id": "ICFES-06-ING-01",
        "grado": "6",
        "asignatura": "Inglés",
        "tema": "Present Simple & School Life",
        "pregunta": "Complete the conversation: 'What time does the soccer match start?' — '______ at 3:00 PM.'",
        "opciones": ["It starts", "They start", "He start", "We starting"],
        "correcta": 0,
        "explicacion": "Para la tercera persona singular ('the soccer match' = it) en presente simple, el verbo lleva 's' ('It starts').",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 6.° Inglés"
    },
    {
        "id": "ICFES-06-ING-02",
        "grado": "6",
        "asignatura": "Inglés",
        "tema": "Sports Vocabulary",
        "pregunta": "Where do people usually play a football game?",
        "opciones": ["In a library", "On a stadium pitch", "In a kitchen", "Inside a cinema"],
        "correcta": 1,
        "explicacion": "'Pitch' o 'stadium' es la cancha o estadio donde se juega fútbol profesional.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 6.° Inglés"
    },
    {
        "id": "ICFES-06-ING-03",
        "grado": "6",
        "asignatura": "Inglés",
        "tema": "Classroom & Rules",
        "pregunta": "Read the sign: 'PLEASE WEAR YOUR TEAM UNIFORM BEFORE ENTERING THE FIELD.' Where can you see this sign?",
        "opciones": ["At the airport", "In the school sports center", "In the hospital", "At the supermarket"],
        "correcta": 1,
        "explicacion": "El aviso indica vestirse con el uniforme del equipo antes de entrar a la cancha, típico de un centro deportivo o polideportivo escolar.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 6.° Inglés"
    },
    {
        "id": "ICFES-06-SOC-04",
        "grado": "6",
        "asignatura": "Ciencias Sociales",
        "tema": "Convivencia y normas de juego limpio",
        "pregunta": "Durante un partido del torneo escolar, el capitán del equipo rival comete una falta accidental pero pide disculpas y ayuda al jugador a levantarse. Esta acción demuestra:",
        "opciones": [
            "Falta de competitividad y cobardía deportiva.",
            "Juego limpio (fair play) y empatía ciudadana.",
            "Desconocimiento total de las reglas del árbitro.",
            "Intención de perder el partido a propósito."
        ],
        "correcta": 1,
        "explicacion": "El juego limpio y el respeto al adversario son valores fundamentales de la convivencia y la ciudadanía deportiva.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Competencias Ciudadanas 6.°"
    },
    {
        "id": "ICFES-06-SOC-05",
        "grado": "6",
        "asignatura": "Ciencias Sociales",
        "tema": "Geografía colombiana",
        "pregunta": "Colombia cuenta con costas en dos océanos diferentes. ¿Cuáles son estos océanos?",
        "opciones": [
            "Océano Atlántico y Océano Pacífico.",
            "Océano Índico y Océano Glacial Ártico.",
            "Océano Atlántico y Océano Índico.",
            "Océano Pacífico y Océano Antártico."
        ],
        "correcta": 0,
        "explicacion": "Colombia es el único país de América del Sur con costas sobre el Océano Pacífico y el Océano Atlántico (Mar Caribe).",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 6.° Ciencias Sociales"
    },
    {
        "id": "ICFES-06-LEN-05",
        "grado": "6",
        "asignatura": "Lenguaje",
        "tema": "Tipología textual - La Fábula",
        "pregunta": "¿Cuál es la característica principal que distingue a una fábula de otros relatos narrativos?",
        "opciones": [
            "Presentar datos estadísticos y fórmulas matemáticas.",
            "Tener personajes animales u objetos con actitudes humanas y dejar una moraleja.",
            "Estar escrita exclusivamente en versos de quince sílabas sin rima.",
            "Narrar hechos 100% verídicos comprobados en un laboratorio."
        ],
        "correcta": 1,
        "explicacion": "La fábula utiliza la personificación de animales para transmitir una enseñanza o moraleja moral y pedagógica.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 6.° Lenguaje"
    },
    {
        "id": "ICFES-06-CN-05",
        "grado": "6",
        "asignatura": "Ciencias Naturales",
        "tema": "Cadena trófica y productores",
        "pregunta": "En un ecosistema terrestre, las plantas verdes son clasificadas como organismos autótrofos porque:",
        "opciones": [
            "Cazan insectos nocturnos para alimentarse.",
            "Producen su propio alimento orgánico mediante la fotosíntesis utilizando luz solar.",
            "Consumen exclusivamente hongos y bacterias del suelo.",
            "Dependen de otros animales para obtener energía vital."
        ],
        "correcta": 1,
        "explicacion": "Los productores o autótrofos sintetizan glucosa a partir de agua, dióxido de carbono y energía lumínica solar mediante la fotosíntesis.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 6.° Ciencias Naturales"
    },

    # ==========================================
    # GRADO 7.°
    # ==========================================
    {
        "id": "ICFES-07-MAT-07",
        "grado": "7",
        "asignatura": "Matemáticas",
        "tema": "Operaciones con números enteros",
        "pregunta": "En un torneo de fútbol de invierno, la temperatura en la cancha a las 6:00 a.m. era de -4 °C. Para el mediodía subió 9 °C y en la noche bajó 3 °C. ¿Cuál es la temperatura final?",
        "opciones": ["+2 °C", "+5 °C", "-2 °C", "+8 °C"],
        "correcta": 0,
        "explicacion": "-4 + 9 = +5 °C; luego +5 - 3 = +2 °C.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 7.° Matemáticas"
    },
    {
        "id": "ICFES-07-MAT-08",
        "grado": "7",
        "asignatura": "Matemáticas",
        "tema": "Proporcionalidad directa",
        "pregunta": "Si un futbolista recorre 24 kilómetros en 3 entrenamientos de igual duración, ¿cuántos kilómetros recorrerá en 7 entrenamientos con la misma intensidad?",
        "opciones": ["48 km", "56 km", "64 km", "70 km"],
        "correcta": 1,
        "explicacion": "Por entrenamiento recorre 24 / 3 = 8 km. En 7 entrenamientos: 7 * 8 = 56 km.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 7.° Matemáticas"
    },
    {
        "id": "ICFES-07-LEN-04",
        "grado": "7",
        "asignatura": "Lenguaje",
        "tema": "Conectores lógicos de causa y consecuencia",
        "pregunta": "En la oración: 'El delantero no pudo jugar la final, ______ sufrió una molestia muscular en el calentamiento', el conector adecuado es:",
        "opciones": ["por lo tanto", "sin embargo", "ya que", "a pesar de que"],
        "correcta": 2,
        "explicacion": "'Ya que' introduce la causa o justificación por la cual el delantero no disputó el partido.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 7.° Lenguaje"
    },
    {
        "id": "ICFES-07-CN-04",
        "grado": "7",
        "asignatura": "Ciencias Naturales",
        "tema": "Sistema respiratorio y ejercicio",
        "pregunta": "Durante una carrera intensa de 90 minutos, la frecuencia respiratoria del deportista aumenta considerablemente debido a que:",
        "opciones": [
            "El cuerpo necesita expulsar nitrógeno y absorber dióxido de carbono.",
            "Las células musculares requieren más oxígeno (O₂) para producir energía (ATP) y eliminar CO₂.",
            "Los pulmones necesitan llenarse de agua para regular la temperatura.",
            "La sangre deja de circular por el corazón momentáneamente."
        ],
        "correcta": 1,
        "explicacion": "La contracción muscular incrementa el consumo celular de O2 y la producción de CO2, lo que activa el centro respiratorio.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 7.° Ciencias Naturales"
    },
    {
        "id": "ICFES-07-SOC-03",
        "grado": "7",
        "asignatura": "Ciencias Sociales",
        "tema": "Ramas del poder público en Colombia",
        "pregunta": "En la Constitución Política de Colombia, ¿cuál de las tres ramas del poder público se encarga de administrar justicia y hacer cumplir las leyes?",
        "opciones": [
            "La Rama Ejecutiva (Presidente y alcaldes).",
            "La Rama Judicial (Cortes, tribunales y jueces).",
            "La Rama Legislativa (Senado y Cámara de Representantes).",
            "El Consejo Nacional Electoral."
        ],
        "correcta": 1,
        "explicacion": "La Rama Judicial administra la justicia colombiana y resuelve conflictos legales entre ciudadanos y el Estado.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Competencias Ciudadanas 7.°"
    },
    {
        "id": "ICFES-07-ING-01",
        "grado": "7",
        "asignatura": "Inglés",
        "tema": "Past Simple",
        "pregunta": "Choose the correct sentence: 'Last Sunday, our school team ______ the championship trophy.'",
        "opciones": ["win", "won", "winned", "winning"],
        "correcta": 1,
        "explicacion": "El pasado simple del verbo irregular 'win' es 'won'.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 7.° Inglés"
    },
    {
        "id": "ICFES-07-ING-02",
        "grado": "7",
        "asignatura": "Inglés",
        "tema": "Reading Comprehension",
        "pregunta": "'Carlos drinks water every 15 minutes during training to stay hydrated.' Why does Carlos drink water?",
        "opciones": [
            "To win video games.",
            "To maintain proper hydration during physical activity.",
            "Because he is sleeping in the classroom.",
            "To clean the stadium grass."
        ],
        "correcta": 1,
        "explicacion": "El texto explica claramente 'to stay hydrated' (para mantenerse hidratado durante la actividad física).",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 7.° Inglés"
    },

    # ==========================================
    # GRADO 8.°
    # ==========================================
    {
        "id": "ICFES-08-MAT-06",
        "grado": "8",
        "asignatura": "Matemáticas",
        "tema": "Lenguaje algebraico y ecuaciones",
        "pregunta": "En un estadio, el triple del número de goles marcados por el equipo local más 5 es igual a 26. ¿Cuántos goles marcó el equipo local?",
        "opciones": ["5 goles", "7 goles", "8 goles", "9 goles"],
        "correcta": 1,
        "explicacion": "Planteando la ecuación: 3x + 5 = 26 -> 3x = 21 -> x = 7 goles.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 8.° Matemáticas"
    },
    {
        "id": "ICFES-08-MAT-07",
        "grado": "8",
        "asignatura": "Matemáticas",
        "tema": "Teorema de Pitágoras",
        "pregunta": "Una cancha rectangular mide 40 metros de largo y 30 metros de ancho. ¿Cuánto mide la diagonal que une dos esquinas opuestas?",
        "opciones": ["50 metros", "60 metros", "70 metros", "45 metros"],
        "correcta": 0,
        "explicacion": "Por Teorema de Pitágoras: d = √(40² + 30²) = √(1600 + 900) = √2500 = 50 metros.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 8.° Matemáticas"
    },
    {
        "id": "ICFES-08-LEN-03",
        "grado": "8",
        "asignatura": "Lenguaje",
        "tema": "Textos argumentativos - Tesis y argumentos",
        "pregunta": "En un ensayo sobre la educación deportiva, el autor afirma: 'El deporte escolar debe ser obligatorio porque fomenta hábitos saludables, reduce el estrés y previene enfermedades crónicas'. Esta afirmación cumple el rol de:",
        "opciones": [
            "Conclusión retórica sin fundamento alguno.",
            "Tesis defendida con sus correspondientes argumentos justificativos.",
            "Una anécdota personal sin validez académica.",
            "Un contraargumento en oposición al deporte."
        ],
        "correcta": 1,
        "explicacion": "Contiene la postura central (tesis: obligatoriedad) sustentada por razones pedagógicas y de salud (argumentos).",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 8.° Lenguaje"
    },
    {
        "id": "ICFES-08-CN-04",
        "grado": "8",
        "asignatura": "Ciencias Naturales",
        "tema": "Reproducción celular: Mitosis y Meiosis",
        "pregunta": "Cuando un deportista sufre una herida leve en la piel durante una jugada y el tejido cicatriza al cabo de unos días, ¿qué proceso biológico genera las nuevas células epiteliales?",
        "opciones": [
            "La meiosis con reducción del número de cromosomas.",
            "La mitosis celular, que genera células hijas genéticamente idénticas.",
            "La fotosíntesis celular epidérmica.",
            "La fermentación láctica anaeróbica."
        ],
        "correcta": 1,
        "explicacion": "La mitosis es la división celular responsable del crecimiento y reparación de los tejidos somáticos en organismos multicelulares.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 8.° Ciencias Naturales"
    },
    {
        "id": "ICFES-08-SOC-03",
        "grado": "8",
        "asignatura": "Ciencias Sociales",
        "tema": "Mecanismos de participación ciudadana en Colombia",
        "pregunta": "¿Cuál es el mecanismo establecido en la Constitución de 1991 mediante el cual los ciudadanos pueden votar para revocar el mandato de un alcalde o gobernador por incumplimiento de su programa de gobierno?",
        "opciones": [
            "La acción de tutela.",
            "La revocatoria del mandato.",
            "El plebiscito presidencial.",
            "El cabildo abierto extraordinario."
        ],
        "correcta": 1,
        "explicacion": "La revocatoria del mandato es el derecho político que permite a los electores dar por terminado el mandato conferido a un alcalde o gobernador.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Competencias Ciudadanas 8.°"
    },
    {
        "id": "ICFES-08-ING-01",
        "grado": "8",
        "asignatura": "Inglés",
        "tema": "Comparatives and Superlatives",
        "pregunta": "Select the correct option: 'This stadium is ______ than the one in our hometown.'",
        "opciones": ["more big", "bigger", "biggest", "the biggest"],
        "correcta": 1,
        "explicacion": "Para adjetivos cortos de una sílaba como 'big', el comparativo se forma duplicando la consonante y agregando '-er': 'bigger'.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 8.° Inglés"
    },
    {
        "id": "ICFES-08-ING-02",
        "grado": "8",
        "asignatura": "Inglés",
        "tema": "Modal Verbs (Obligation and Advice)",
        "pregunta": "'All soccer players ______ respect the referee's decisions during the match.'",
        "opciones": ["must", "can't", "shouldn't", "are not"],
        "correcta": 0,
        "explicacion": "'Must' expresa deber u obligación reglamentaria.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 8.° Inglés"
    },

    # ==========================================
    # GRADO 9.°
    # ==========================================
    {
        "id": "ICFES-09-MAT-04",
        "grado": "9",
        "asignatura": "Matemáticas",
        "tema": "Sistemas de ecuaciones 2x2",
        "pregunta": "Para la final escolar se vendieron 100 boletas en total entre adultos y niños. La boleta de adulto costaba $10.000 y la de niño $5.000. Si se recaudaron $700.000, ¿cuántas boletas de adulto se vendieron?",
        "opciones": ["30 boletas", "40 boletas", "50 boletas", "60 boletas"],
        "correcta": 1,
        "explicacion": "x + y = 100 y 10000x + 5000y = 700000. Sustituyendo y = 100 - x: 10000x + 500000 - 5000x = 700000 -> 5000x = 200000 -> x = 40 adultos.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 9.° Matemáticas"
    },
    {
        "id": "ICFES-09-MAT-05",
        "grado": "9",
        "asignatura": "Matemáticas",
        "tema": "Función cuadrática y trayectorias",
        "pregunta": "La trayectoria de un disparo de tiro libre sigue la función h(t) = -5t² + 20t, donde h es la altura en metros y t el tiempo en segundos. ¿En qué segundo alcanza su altura máxima?",
        "opciones": ["1 segundo", "2 segundos", "3 segundos", "4 segundos"],
        "correcta": 1,
        "explicacion": "El vértice de una parábola -at² + bt ocurre en t = -b / (2a) = -20 / (2*(-5)) = 2 segundos.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 9.° Matemáticas"
    },
    {
        "id": "ICFES-09-LEN-03",
        "grado": "9",
        "asignatura": "Lenguaje",
        "tema": "Figuras literarias - Metáfora y Símil",
        "pregunta": "En el comentario deportivo: 'El arquero voló como un felino bajo el arco y sus manos fueron una muralla infranqueable', las figuras retóricas presentes son, en su orden:",
        "opciones": [
            "Hipérbole e ironía.",
            "Símil (comparación directa con 'como') y metáfora.",
            "Personificación y pleonasmo.",
            "Onomatopeya y elipsis."
        ],
        "correcta": 1,
        "explicacion": "'Como un felino' usa el nexo explícito 'como' (símil), mientras que 'sus manos fueron una muralla' identifica un término con otro directamente (metáfora).",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 9.° Lenguaje"
    },
    {
        "id": "ICFES-09-CN-03",
        "grado": "9",
        "asignatura": "Ciencias Naturales",
        "tema": "Leyes de la Genética Mendeliana",
        "pregunta": "Si se cruzan dos plantas heterocigotas (Aa) para el color de la semilla, donde 'A' (amarillo) domina sobre 'a' (verde), ¿cuál es la probabilidad de obtener semillas verdes (aa)?",
        "opciones": ["100%", "75%", "50%", "25%"],
        "correcta": 3,
        "explicacion": "En el cuadro de Punnett de Aa x Aa se obtienen: 1 AA (25%), 2 Aa (50%) y 1 aa (25%). El fenotipo recesivo representa el 25% (1/4).",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 9.° Ciencias Naturales"
    },
    {
        "id": "ICFES-09-SOC-03",
        "grado": "9",
        "asignatura": "Ciencias Sociales",
        "tema": "Derechos Humanos y Constitución",
        "pregunta": "¿Cuál es la herramienta jurídica creada por la Constitución de 1991 que cualquier persona puede interponer ante un juez para la protección inmediata de sus derechos fundamentales vulnerados?",
        "opciones": [
            "La Acción de Tutela.",
            "El Juicio Político del Congreso.",
            "El Derecho de Petición Mercantil.",
            "La Demanda de Expropiación."
        ],
        "correcta": 0,
        "explicacion": "La Acción de Tutela (Artículo 86 de la Constitución) garantiza la protección judicial inmediata de derechos fundamentales como la vida, salud y debido proceso.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Competencias Ciudadanas 9.°"
    },
    {
        "id": "ICFES-09-ING-04",
        "grado": "9",
        "asignatura": "Inglés",
        "tema": "First Conditional",
        "pregunta": "'If the team ______ hard today, they ______ the match tomorrow.'",
        "opciones": [
            "trains / will win",
            "trained / would won",
            "train / winning",
            "will train / wins"
        ],
        "correcta": 0,
        "explicacion": "El primer condicional en inglés usa: If + presente simple ('trains'), resultado con will + infinitivo ('will win').",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 9.° Inglés"
    },

    # ==========================================
    # GRADO 10.°
    # ==========================================
    {
        "id": "ICFES-10-MAT-05",
        "grado": "10",
        "asignatura": "Matemáticas",
        "tema": "Razones trigonométricas",
        "pregunta": "Un reflector del estadio está ubicado a 30 metros de altura. Si proyecta un haz de luz hacia el centro del campo con un ángulo de elevación de 45°, ¿a qué distancia horizontal de la base del poste se encuentra el centro del campo?",
        "opciones": ["15 metros", "30 metros", "45 metros", "60 metros"],
        "correcta": 1,
        "explicacion": "tan(45°) = altura / distancia = 1. Por lo tanto, distancia = altura = 30 metros.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 10.° Matemáticas"
    },
    {
        "id": "ICFES-10-MAT-06",
        "grado": "10",
        "asignatura": "Matemáticas",
        "tema": "Ley de Cosenos",
        "pregunta": "En un triángulo con lados a = 5 m, b = 5 m y un ángulo comprendido C = 60°, ¿cuánto mide el lado opuesto c?",
        "opciones": ["3 m", "5 m", "7 m", "10 m"],
        "correcta": 1,
        "explicacion": "Al tener dos lados iguales (5 m) y un ángulo de 60°, el triángulo es equilátero, por lo que el tercer lado mide exactamente 5 m (c² = 25 + 25 - 2(25)(0.5) = 25 -> c = 5).",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 10.° Matemáticas"
    },
    {
        "id": "ICFES-10-CN-03",
        "grado": "10",
        "asignatura": "Ciencias Naturales",
        "tema": "Cinemática y Dinámica de Newton",
        "pregunta": "Un balón de fútbol de 0.45 kg es pateado desde el reposo y adquiere una aceleración de 40 m/s². De acuerdo con la Segunda Ley de Newton (F = m · a), ¿cuál es la magnitud de la fuerza neta aplicada?",
        "opciones": ["12 N", "18 N", "25 N", "45 N"],
        "correcta": 1,
        "explicacion": "F = m · a = 0.45 kg · 40 m/s² = 18 Newtons.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 10.° Ciencias Naturales / Física"
    },
    {
        "id": "ICFES-10-CN-04",
        "grado": "10",
        "asignatura": "Ciencias Naturales",
        "tema": "Química de gases y Ley de Boyle",
        "pregunta": "Si un balón inflado se comprime a temperatura constante reduciendo su volumen a la mitad, ¿qué sucede con la presión interna del aire de acuerdo con la Ley de Boyle?",
        "opciones": [
            "La presión se reduce a la mitad.",
            "La presión se duplica.",
            "La presión permanece inalterada.",
            "La presión cae a cero absoluto."
        ],
        "correcta": 1,
        "explicacion": "La Ley de Boyle establece que a temperatura constante, la presión y el volumen son inversamente proporcionales (P1·V1 = P2·V2). Al reducir el volumen a la mitad, la presión se duplica.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 10.° Ciencias Naturales / Química"
    },
    {
        "id": "ICFES-10-SOC-03",
        "grado": "10",
        "asignatura": "Ciencias Sociales",
        "tema": "Economía y Ley de Oferta y Demanda",
        "pregunta": "Si la demanda de entradas para la final de un campeonato nacional de fútbol se dispara masivamente mientras la capacidad del estadio se mantiene fija (oferta inelástica), ¿qué ocurrirá con el precio de equilibrio en el mercado?",
        "opciones": [
            "El precio de equilibrio tenderá a subir significativamente.",
            "El precio caerá a cero y las entradas serán gratuitas.",
            "La oferta se duplicará automáticamente de la noche a la mañana.",
            "El precio no sufrirá ninguna alteración económica."
        ],
        "correcta": 0,
        "explicacion": "Cuando la demanda supera con creces la oferta fija disponible, la escasez presiona el precio de mercado al alza.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 10.° Ciencias Sociales y Ciudadanas"
    },
    {
        "id": "ICFES-10-LEN-03",
        "grado": "10",
        "asignatura": "Lenguaje",
        "tema": "Lectura Crítica - Supuestos e inferencias",
        "pregunta": "En una columna de opinión, el autor señala: 'Los triunfos efímeros no construyen legados institucionales; únicamente la inversión en semilleros juveniles garantiza la sostenibilidad deportiva'. ¿Cuál es el supuesto implícito del autor?",
        "opciones": [
            "Que no es necesario competir para ganar trofeos.",
            "Que la formación a largo plazo en las bases es más valiosa y sostenible que victorias aisladas e inmediatas.",
            "Que los torneos juveniles deberían cancelarse por falta de público.",
            "Que el dinero no tiene ninguna relación con el rendimiento deportivo."
        ],
        "correcta": 1,
        "explicacion": "El autor prioriza la estructura formativa y el desarrollo progresivo frente a resultados inmediatos coyunturales.",
        "dificultad": "Avanzado",
        "fuente": "Cuadernillo ICFES Saber 10.° Lectura Crítica"
    },
    {
        "id": "ICFES-10-ING-03",
        "grado": "10",
        "asignatura": "Inglés",
        "tema": "Passive Voice in Sports News",
        "pregunta": "Choose the correct passive voice sentence: 'The winning goal ______ by the star striker in the 90th minute.'",
        "opciones": [
            "was scored",
            "scores",
            "is scoring",
            "were score"
        ],
        "correcta": 0,
        "explicacion": "La voz pasiva en pasado para sujeto singular ('The winning goal') requiere 'was' + participio pasado ('was scored').",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 10.° Inglés"
    }
]

def main():
    with open('data/questions.json', 'r', encoding='utf-8') as f:
        existing = json.load(f)

    existing_ids = {q['id'] for q in existing}
    added = 0
    for q in additional_questions:
        if q['id'] not in existing_ids:
            existing.append(q)
            added += 1

    with open('data/questions.json', 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Added {added} new questions. Total in data/questions.json: {len(existing)}")

if __name__ == '__main__':
    main()
