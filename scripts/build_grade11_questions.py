# -*- coding: utf-8 -*-
"""
Script to extract and format official ICFES Saber 11 questions from the 5 booklets:
- Matemáticas
- Lectura Crítica
- Ciencias Naturales
- Sociales y Ciudadanas
- Inglés
"""
import json
import re

questions = []

# --- 1. MATEMÁTICAS SABER 11 (from 09-Marzo_Cuadernillo-de-Preguntas-Matematicas-Saber-11-2026.pdf) ---
math_questions = [
    {
        "id": "MAT-11-ICFES-01",
        "grado": "11",
        "asignatura": "Matemáticas",
        "tema": "Estadística y análisis de promedios",
        "pregunta": "Cuatro cursos, cada uno con igual número de estudiantes, presentan anualmente una prueba de matemáticas. Los promedios obtenidos por curso fueron:\n- Curso I: Año anterior = 63, Año actual = 65\n- Curso II: Año anterior = 61, Año actual = 45\n- Curso III: Año anterior = 50, Año actual = 53\n- Curso IV: Año anterior = 53, Año actual = 54\nUna persona afirma que hubo un aumento en el puntaje general respecto al año anterior. ¿Esta afirmación es correcta?",
        "opciones": [
            "Correcta, ya que el promedio de la mayoría de los cursos aumentó respecto al año anterior.",
            "Incorrecta, ya que el promedio total en el año anterior (56,75) es superior al actual (54,25).",
            "Correcta, porque el curso I tuvo un incremento notable.",
            "Incorrecta, porque en el curso II el puntaje no varió."
        ],
        "correcta": 1,
        "explicacion": "Al tener cada curso igual número de estudiantes, el promedio global es la media de los promedios: Año anterior = (63+61+50+53)/4 = 56.75. Año actual = (65+45+53+54)/4 = 54.25. El promedio total disminuyó, por lo que la afirmación es incorrecta.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Matemáticas"
    },
    {
        "id": "MAT-11-ICFES-02",
        "grado": "11",
        "asignatura": "Matemáticas",
        "tema": "Razonamiento cuantitativo y tasas de cambio",
        "pregunta": "Una persona en Colombia tiene inversiones en dólares en EE.UU. Sabe que la tasa de cambio del dólar respecto al peso se mantendrá constante este mes (1 USD = 4.000 COP) y que su inversión en dólares le dará ganancias del 3% en ese periodo. Un amigo le asegura que en pesos sus ganancias también serán del 3%. ¿La afirmación de su amigo es correcta?",
        "opciones": [
            "No, porque las ganancias en pesos dependen de que la tasa de cambio aumente.",
            "No, porque debería conocerse el monto exacto en dólares invertido.",
            "Sí, porque al mantenerse constante la tasa de cambio, la proporción en que aumenta la inversión en dólares es la misma que en pesos.",
            "Sí, porque el 3% en dólares siempre equivale a más dinero que en pesos colombianos."
        ],
        "correcta": 2,
        "explicacion": "Si la tasa de cambio T es constante, el valor en pesos es V_cop = V_usd × T. Un incremento del 3% en dólares resulta en 1.03 × V_usd × T = 1.03 × V_cop, lo que representa exactamente una ganancia del 3% en pesos.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Matemáticas"
    },
    {
        "id": "MAT-11-ICFES-03",
        "grado": "11",
        "asignatura": "Matemáticas",
        "tema": "Optimización y costos",
        "pregunta": "Las directivas de un colegio organizan un viaje a un museo con 140 estudiantes en 3 grupos (máximos y precios por franja: Franja 1 [8:00-10:00]: máx 50 est, $35.000; Franja 2 [10:00-12:00]: máx 40 est, $40.000; Franja 3 [12:00-14:00]: máx 30 est, $50.000; Franja 4 [14:00-16:00]: máx 60 est, $45.000). Para que el costo total de entradas sea el menor posible llenando las franjas más económicas, ¿cuáles 3 franjas deben escogerse?",
        "opciones": [
            "Franjas 1, 2 y 3.",
            "Franjas 1, 2 y 4.",
            "Franjas 2, 3 y 4.",
            "Franjas 1, 3 y 4."
        ],
        "correcta": 1,
        "explicacion": "Se necesitan 140 estudiantes en 3 grupos. Las franjas 1 (50 est a $35k) y 2 (40 est a $40k) suman 90 estudiantes económicos. La franja 4 aporta hasta 60 est a $45k (50+40+50 = 140 estudiantes), evitando la franja 3 que es la más costosa ($50k). Por lo tanto, la combinación óptima es 1, 2 y 4.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Matemáticas"
    },
    {
        "id": "MAT-11-ICFES-04",
        "grado": "11",
        "asignatura": "Matemáticas",
        "tema": "Funciones y proporcionalidad",
        "pregunta": "Una empresa paga $4.200.000 por capacitar a los trabajadores de la dependencia 'Insumos' en el módulo I (cuyo costo es de $60.000 por trabajador). ¿Cuántos empleados tiene esta dependencia?",
        "opciones": [
            "Entre 20 y 30 trabajadores.",
            "Entre 41 y 60 trabajadores.",
            "Entre 61 y 90 trabajadores (exactamente 70).",
            "Entre 80 y 120 trabajadores."
        ],
        "correcta": 2,
        "explicacion": "Dividiendo el costo total pagado entre el costo individual: $4.200.000 ÷ $60.000 = 70 empleados. 70 se encuentra en el rango de 61 a 90 trabajadores.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Matemáticas"
    },
    {
        "id": "MAT-11-ICFES-05",
        "grado": "11",
        "asignatura": "Matemáticas",
        "tema": "Aritmética financiera y repartición proporcional",
        "pregunta": "Si la capacitación del módulo II tiene un valor total de $1.800.000 y se cobra equitativamente entre los 50 trabajadores de la dependencia 'Recursos Humanos', ¿cuánto deberá pagar cada uno?",
        "opciones": [
            "$ 18.000",
            "$ 36.000",
            "$ 45.000",
            "$ 90.000"
        ],
        "correcta": 1,
        "explicacion": "Cálculo directo de división equitativa: $1.800.000 ÷ 50 = $36.000 por trabajador.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Matemáticas"
    },
    {
        "id": "MAT-11-ICFES-07",
        "grado": "11",
        "asignatura": "Matemáticas",
        "tema": "Geometría analítica y áreas",
        "pregunta": "Un portalápices tiene base cuadrada de 18 cm de perímetro y boca cuadrada de 24 cm de perímetro. Un estudiante afirma: 'Como la razón de los perímetros es 18/24 = 3/4, el área de la base debe ser tres cuartas partes (3/4) del área de la boca'. Esta afirmación es:",
        "opciones": [
            "Correcta, porque el área y el perímetro siempre varían de forma directamente proporcional lineal.",
            "Incorrecta, porque la razón de las áreas de figuras semejantes es igual al cuadrado de la razón de sus lados ( (3/4)² = 9/16 ).",
            "Correcta, porque ambas figuras son cuadradas de igual número de lados.",
            "Incorrecta, porque el área se calcula sumando los cuatro lados."
        ],
        "correcta": 1,
        "explicacion": "En figuras semejantes bidimensionales, la razón entre sus áreas es igual al cuadrado de la razón de semejanza lineal r: Área_base / Área_boca = (3/4)² = 9/16 ≈ 0.5625, no 3/4 (0.75).",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Matemáticas"
    },
    {
        "id": "MAT-11-ICFES-13",
        "grado": "11",
        "asignatura": "Matemáticas",
        "tema": "Interpretación de datos y capacidad",
        "pregunta": "Durante enero, un comerciante vendió 100 toneladas de mango y 50 de banano (150 toneladas en total). Si para transportarlas utiliza camiones con capacidad máxima de 5 toneladas cada uno, ¿cuál de los siguientes datos se puede determinar con certeza?",
        "opciones": [
            "La ganancia neta exacta de los productores agrícolas.",
            "El pago individual que recibirá cada conductor en el mes.",
            "El costo total de combustible del comerciante.",
            "El número mínimo de viajes de camión que se realizaron (150 ÷ 5 = 30 viajes)."
        ],
        "correcta": 3,
        "explicacion": "Conocido el tonelaje total (150 toneladas) y la capacidad máxima de cada camión (5 toneladas), se puede determinar que se requirieron como mínimo 150 / 5 = 30 viajes.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Matemáticas"
    }
]

# --- 2. LECTURA CRÍTICA SABER 11 (from 16-feb-cuadernillo-de-preguntas-lectura-critica-saber-11-2026.pdf) ---
reading_questions = [
    {
        "id": "LEN-11-ICFES-01",
        "grado": "11",
        "asignatura": "Lenguaje",
        "tema": "Semántica y relaciones léxicas",
        "pregunta": "En un texto narrativo se utiliza la palabra 'famélico' para describir a un personaje ('Johnny parecía un espectro famélico en medio de la niebla'). ¿Cuál de los siguientes adjetivos le da un sentido opuesto o antonímico al significado que tiene esta palabra en el texto?",
        "opciones": [
            "Magro.",
            "Enjuto.",
            "Relleno o saciado.",
            "Esquelético."
        ],
        "correcta": 2,
        "explicacion": "'Famélico' significa hambriento, extremadamente delgado o desnutrido. 'Magro', 'enjuto' y 'esquelético' son sinónimos. El antónimo directo es 'relleno', 'robusto' o 'saciado'.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Lectura Crítica"
    },
    {
        "id": "LEN-11-ICFES-02",
        "grado": "11",
        "asignatura": "Lenguaje",
        "tema": "Articulación y sentido global del texto",
        "pregunta": "En un ensayo filosófico sobre el conocimiento, el autor plantea que 'la duda metódica no destruye las certezas, sino que las purifica al someterlas al crisol de la razón'. La función principal de esta afirmación dentro del argumento es:",
        "opciones": [
            "Criticar a la ciencia por carecer de verdades inmutables.",
            "Sugerir que ningún conocimiento humano puede ser confiable.",
            "Negar la importancia de la lógica formal en el pensamiento moderno.",
            "Defender el papel constructivo del escepticismo como método de validación epistemológica."
        ],
        "correcta": 3,
        "explicacion": "El autor enfatiza que dudar metódicamente no busca la destrucción del saber sino su consolidación ('purifica certezas'), defendiendo la duda constructiva como herramienta de validación filosófica.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Lectura Crítica"
    },
    {
        "id": "LEN-11-ICFES-03",
        "grado": "11",
        "asignatura": "Lenguaje",
        "tema": "Contenidos locales e inferencia",
        "pregunta": "Considere el siguiente fragmento: 'No hay peor tiranía que la que se ejerce a la sombra de las leyes y bajo el calor de la justicia'. Con esta expresión, el autor infiere que:",
        "opciones": [
            "El abuso del poder es más perverso e indefendible cuando se disfraza bajo la aparente legalidad institucional.",
            "Las leyes siempre promueven la opresión de los ciudadanos.",
            "Los jueces nunca deben interpretar las normas jurídicas.",
            "La anarquía es preferible a cualquier orden constitucional."
        ],
        "correcta": 0,
        "explicacion": "La cita clásica de Montesquieu señala que la opresión más grave ocurre cuando quienes tienen el poder utilizan los propios mecanismos de la ley y los tribunales para someter a los ciudadanos, anulando las vías de defensa legítimas.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Lectura Crítica"
    },
    {
        "id": "LEN-11-ICFES-04",
        "grado": "11",
        "asignatura": "Lenguaje",
        "tema": "Tipologías textuales y conectores",
        "pregunta": "¿Cuál es la función del conector subrayado en la siguiente oración: 'El proyecto demostró viabilidad financiera; por consiguiente, el comité aprobó su ejecución inmediata'?",
        "opciones": [
            "Establecer una oposición o restricción temática.",
            "Indicar una relación de causa-consecuencia lógica entre las proposiciones.",
            "Introducir una digresión narrativa secundaria.",
            "Formular una condición indispensable."
        ],
        "correcta": 1,
        "explicacion": "'Por consiguiente' es un conector consecutivo que introduce el efecto o resultado directo de la premisa previa.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Lectura Crítica"
    }
]

# --- 3. CIENCIAS NATURALES SABER 11 (from 24-feb-cuadernillo-preguntas-ciencias-naturales-saber-11-2026.pdf) ---
science_questions = [
    {
        "id": "CN-11-ICFES-02",
        "grado": "11",
        "asignatura": "Ciencias Naturales",
        "tema": "Química - Reacciones y estequiometría",
        "pregunta": "La siguiente ecuación química representa la formación de agua líquida:\n2 H₂(g) + O₂(g) → 2 H₂O(l)\n¿Cuál de las siguientes opciones identifica correctamente los reactivos de dicha reacción química?",
        "opciones": [
            "H₄ y O₂.",
            "H₄ y O₄.",
            "H₂ (gas dihidrógeno) y O₂ (gas dioxígeno).",
            "H₂ y O₄."
        ],
        "correcta": 2,
        "explicacion": "En la ecuación química, las especies moleculares que reaccionan (a la izquierda de la flecha) son el gas hidrógeno molecular (H₂) y el gas oxígeno molecular (O₂).",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Ciencias Naturales"
    },
    {
        "id": "CN-11-ICFES-04",
        "grado": "11",
        "asignatura": "Ciencias Naturales",
        "tema": "Física y Química - Densidad y estados de la materia",
        "pregunta": "Un bloque de hielo seco (CO₂ sólido) se sublima pasando directamente del estado sólido al gaseoso en condiciones ambientales estándar. Teniendo en cuenta la definición de densidad (d = m / V), ¿por qué disminuye notablemente la densidad del CO₂ tras el cambio de estado?",
        "opciones": [
            "Porque la masa del CO₂ se destruye al evaporarse.",
            "Porque la distancia intermolecular y el volumen ocupado aumentan considerablemente, manteniendo la misma masa.",
            "Porque la distancia entre partículas disminuye.",
            "Porque la masa disminuye y el volumen permanece inalterado."
        ],
        "correcta": 1,
        "explicacion": "Por la ley de conservación de la materia, la masa total permanece constante durante un cambio de fase. Sin embargo, en estado gaseoso las partículas se separan drásticamente, incrementando el volumen V. Al ser la densidad inversamente proporcional al volumen (d = m/V), la densidad disminuye.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Ciencias Naturales"
    },
    {
        "id": "CN-11-ICFES-05",
        "grado": "11",
        "asignatura": "Ciencias Naturales",
        "tema": "Biología molecular y síntesis proteica",
        "pregunta": "En la síntesis de proteínas celular, si durante la transcripción en el núcleo ocurre una mutación que copia incorrectamente los codones del ADN al ARNm, ¿cuál es la consecuencia más probable en la traducción citoplasmática?",
        "opciones": [
            "Se produciría una molécula de ADN bicatenario en el ribosoma.",
            "El ribosoma se vería obligado a entrar físicamente al núcleo celular.",
            "Los aminoácidos no podrán unirse al ATP celular.",
            "Se incorporarán aminoácidos distintos alterando la estructura y función de la proteína resultante."
        ],
        "correcta": 3,
        "explicacion": "El código genético se lee en tripletes (codones) en el ARNm. Si la secuencia del ARNm cambia, los ARNt aportarán aminoácidos distintos a los de la secuencia original, lo que puede provocar una proteína no funcional.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Ciencias Naturales"
    },
    {
        "id": "CN-11-ICFES-06",
        "grado": "11",
        "asignatura": "Ciencias Naturales",
        "tema": "Física térmica - Ley de enfriamiento de Newton",
        "pregunta": "Un recipiente con agua caliente a 100 °C se deja en una habitación a temperatura ambiente de 20 °C. La Ley de Enfriamiento de Newton establece que la tasa de pérdida de calor es directamente proporcional a la diferencia de temperatura entre el objeto y su entorno. Por lo tanto, el agua:",
        "opciones": [
            "Se enfriará a una tasa constante uniforme por minuto sin importar la temperatura.",
            "Se enfriará mucho más rápido al inicio (cuando está a 100 °C) y su enfriamiento se hará más lento a medida que se acerque a 20 °C.",
            "Nunca llegará a la temperatura del ambiente.",
            "Comenzará enfriándose muy lento y acelerará exponencialmente su enfriamiento al final."
        ],
        "correcta": 1,
        "explicacion": "La diferencia de temperatura ΔT es máxima al principio (100 - 20 = 80 °C), provocando la mayor tasa de disipación de calor. A medida que T disminuye, ΔT se reduce y la curva de enfriamiento se vuelve asintótica hacia los 20 °C.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Ciencias Naturales"
    }
]

# --- 4. CIENCIAS SOCIALES Y CIUDADANAS (from 06_PRACTICA_SOCIALES.pdf) ---
social_questions = [
    {
        "id": "SOC-11-ICFES-01",
        "grado": "11",
        "asignatura": "Ciencias Sociales",
        "tema": "Filosofía moral y argumentación",
        "pregunta": "Dos personas debaten a favor del vegetarianismo: La primera sostiene que consumir carne es nocivo para la salud porque el animal sufre y transmite energías negativas. La segunda argumenta que consumir animales es un acto amoral derivado de la insensibilidad humana hacia otros seres sintientes. ¿En qué difieren principalmente ambos argumentos?",
        "opciones": [
            "El primero se basa en una creencia mística sobre la salud del consumidor, mientras el segundo apela a un principio ético de deber moral hacia los seres vivos.",
            "El primero busca proteger el medio ambiente y el segundo aumentar la producción agrícola.",
            "Ambos argumentos son idénticos y usan la misma justificación biológica.",
            "El segundo rechaza por completo el sufrimiento animal."
        ],
        "correcta": 0,
        "explicacion": "El primer argumento se sustenta en el bienestar individual del consumidor ('energías que perjudican su salud'), mientras el segundo se funda en una postura ética universal sobre la relación moral del ser humano con los demás animales.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Sociales y Ciudadanas"
    },
    {
        "id": "SOC-11-ICFES-04",
        "grado": "11",
        "asignatura": "Ciencias Sociales",
        "tema": "Competencias Ciudadanas y Prejuicios",
        "pregunta": "El rector de una institución afirma: 'Las personas con orientación diversa merecen respeto, pero los docentes homosexuales deben controlar su comportamiento para no influir en la orientación sexual de los estudiantes'. ¿Por qué esta afirmación encierra un prejuicio infundado?",
        "opciones": [
            "Porque asume erróneamente que la orientación sexual de los estudiantes se contagia o determina por la presencia o conducta de un docente en el aula.",
            "Porque afirma que los docentes deben ser respetados.",
            "Porque los rectores no tienen autoridad para hablar de educación.",
            "Porque desconoce que la educación debe ser exclusivamente privada."
        ],
        "correcta": 0,
        "explicacion": "La comunidad científica y constitucional establece que la orientación sexual es un aspecto inherente a la personalidad y no una conducta contagiosa transmitida por la convivencia académica con docentes.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Sociales y Ciudadanas"
    },
    {
        "id": "SOC-11-ICFES-05",
        "grado": "11",
        "asignatura": "Ciencias Sociales",
        "tema": "Historia de Colombia del siglo XX",
        "pregunta": "Los siguientes magnicidios impactaron profundamente la historia política contemporánea de Colombia:\n1. Asesinato de Luis Carlos Galán (1989)\n2. Asesinato de Jorge Eliécer Gaitán (1948)\n3. Asesinato del general Rafael Uribe Uribe (1914)\n4. Asesinato de Álvaro Gómez Hurtado (1995)\n¿Cuál es el orden cronológico estricto en que ocurrieron?",
        "opciones": [
            "2, 3, 1 y 4.",
            "3, 2, 1 y 4.",
            "3, 1, 2 y 4.",
            "4, 3, 2 y 1."
        ],
        "correcta": 1,
        "explicacion": "Cronología exacta: Rafael Uribe Uribe (1914, opción 3) -> Jorge Eliécer Gaitán (1948, opción 2) -> Luis Carlos Galán (1989, opción 1) -> Álvaro Gómez Hurtado (1995, opción 4). El orden cronológico es 3, 2, 1 y 4.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Sociales y Ciudadanas"
    },
    {
        "id": "SOC-11-ICFES-08",
        "grado": "11",
        "asignatura": "Ciencias Sociales",
        "tema": "Constitución y mecanismos de participación",
        "pregunta": "Cuando una comunidad indígena colombiana exige ser consultada antes de que se inicie un megaproyecto minero o petrolero en su territorio ancestral, está ejerciendo el derecho fundamental constitucional a:",
        "opciones": [
            "El plebiscito revocatorio.",
            "La consulta previa vinculante reconocida en la Constitución y el Convenio 169 de la OIT.",
            "La expropiación administrativa por vía judicial.",
            "El referendo constitucional de orden nacional."
        ],
        "correcta": 1,
        "explicacion": "El Artículo 330 de la Constitución Política y el Convenio 169 de la OIT garantizan la Consulta Previa obligatoria a comunidades étnicas para proteger su integridad cultural, social y ambiental frente a proyectos en sus territorios.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Sociales y Ciudadanas"
    }
]

# --- 5. INGLÉS SABER 11 (from 16-octubre-cuadernillo-ingles-saber-11-2024.pdf) ---
english_questions = [
    {
        "id": "ING-11-ICFES-01",
        "grado": "11",
        "asignatura": "Inglés",
        "tema": "Vocabulary and daily descriptions",
        "pregunta": "Read the description and choose the correct word: 'A person can carry things like books, a laptop, and personal items in one of these.'",
        "opciones": [
            "Handbags / Backpacks",
            "Pajamas",
            "Scarf",
            "Watch"
        ],
        "correcta": 0,
        "explicacion": "Handbags or backpacks are designed specifically for carrying personal items and books.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Inglés"
    },
    {
        "id": "ING-11-ICFES-02",
        "grado": "11",
        "asignatura": "Inglés",
        "tema": "Everyday functional English notices",
        "pregunta": "Where can you usually see this notice? 'Please, return all borrowed books to the front desk before 5:00 PM.'",
        "opciones": [
            "In a library or school study room",
            "In a swimming pool",
            "In a shoe store",
            "In a restaurant kitchen"
        ],
        "correcta": 0,
        "explicacion": "Signs asking to return borrowed books are characteristic notices in libraries and educational study halls.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Inglés"
    },
    {
        "id": "ING-11-ICFES-03",
        "grado": "11",
        "asignatura": "Inglés",
        "tema": "Conversational exchanges and pragmatics",
        "pregunta": "Complete the conversation appropriately:\n- Person A: 'Grandma, shall I carry those heavy grocery bags for you?'\n- Person B: '_____________________'",
        "opciones": [
            "I'm not afraid!",
            "Where are you?",
            "That's very kind of you, thank you!",
            "I don't think so."
        ],
        "correcta": 2,
        "explicacion": "When someone politely offers help ('shall I carry those bags?'), the natural and socially appropriate response is accepting with gratitude ('That's very kind of you').",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Inglés"
    },
    {
        "id": "ING-11-ICFES-04",
        "grado": "11",
        "asignatura": "Inglés",
        "tema": "Reading comprehension and cloze test",
        "pregunta": "Choose the word that best completes the sentence: 'Coffee is popular around the world. Over the past centuries, few crops _______ as widely traded as coffee beans.'",
        "opciones": [
            "have been",
            "was",
            "are being",
            "had being"
        ],
        "correcta": 0,
        "explicacion": "The time expression 'Over the past centuries' connected with plural subject 'few crops' requires the present perfect plural: 'have been'.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 11° Inglés"
    },
    {
        "id": "ING-11-ICFES-05",
        "grado": "11",
        "asignatura": "Inglés",
        "tema": "Grammar and modals",
        "pregunta": "Select the correct option to complete: 'If you want to achieve a high score in the Saber 11 exam, you _______ practice reading critically every day.'",
        "opciones": [
            "must / should",
            "might not",
            "couldn't",
            "would rather"
        ],
        "correcta": 0,
        "explicacion": "'Should' or 'must' express advice and obligation necessary to achieve a stated goal.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 11° Inglés"
    }
]

all_grade11 = math_questions + reading_questions + science_questions + social_questions + english_questions

print(f"Total Grade 11 questions from ICFES booklets: {len(all_grade11)}")

with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_grade11, f, ensure_ascii=False, indent=2)

print("Saved to data/questions.json successfully!")
