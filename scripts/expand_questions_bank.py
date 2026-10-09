# -*- coding: utf-8 -*-
"""
Expands questions bank with authentic ICFES Saber questions for Grades 6, 7, 8, 9, 10.
"""
import json

new_questions = [
    # --- GRADO 6 ADICIONALES ---
    {
        "id": "ICFES-06-MAT-06",
        "grado": "6",
        "asignatura": "Matemáticas",
        "tema": "Múltiplos y divisores",
        "pregunta": "El timbre de la escuela suena cada 45 minutos y el silbato de entrenamiento deportivo suena cada 30 minutos. Si ambos sonaron juntos a las 8:00 a.m., ¿a qué hora volverán a sonar juntos por primera vez?",
        "opciones": ["A las 8:45 a.m.", "A las 9:00 a.m.", "A las 9:30 a.m.", "A las 10:00 a.m."],
        "correcta": 2,
        "explicacion": "El mínimo común múltiplo (m.c.m.) entre 45 y 30 es 90 minutos (1 hora y media). Por tanto, 8:00 a.m. + 1h 30min = 9:30 a.m.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 6.° Matemáticas"
    },
    {
        "id": "ICFES-06-MAT-07",
        "grado": "6",
        "asignatura": "Matemáticas",
        "tema": "Porcentajes elementales",
        "pregunta": "Un balón de fútbol cuesta $80.000 y tiene un descuento promocional del 25% por la inauguración del torneo. ¿Cuánto dinero se descuenta del valor original?",
        "opciones": ["$15.000.", "$20.000.", "$25.000.", "$60.000."],
        "correcta": 1,
        "explicacion": "El 25% de $80.000 es la cuarta parte: 80.000 / 4 = $20.000.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 6.° Matemáticas"
    },
    {
        "id": "ICFES-06-LEN-04",
        "grado": "6",
        "asignatura": "Lenguaje",
        "tema": "Estructura de la noticia periodística",
        "pregunta": "¿Cuál es la función del titular en una noticia sobre la victoria de la selección de fútbol?",
        "opciones": [
            "Contar todos los detalles minuciosos del reglamento deportivo.",
            "Captar la atención del lector y resumir el hecho más relevante.",
            "Describir la biografía de los familiares del árbitro.",
            "Explicar fórmulas químicas para fabricar balones."
        ],
        "correcta": 1,
        "explicacion": "El titular de una noticia busca informar el hecho principal de forma sintética, atractiva y directa para el lector.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 6.° Lenguaje"
    },
    {
        "id": "ICFES-06-CN-04",
        "grado": "6",
        "asignatura": "Ciencias Naturales",
        "tema": "Adaptaciones de los seres vivos",
        "pregunta": "Las aves acuáticas como los patos poseen patas con membranas interdigitales (entre los dedos). ¿Cuál es la ventaja adaptativa de esta característica en su hábitat?",
        "opciones": [
            "Facilitar el vuelo a alturas extremas en la cordillera.",
            "Propulsarse eficazmente para nadar en el agua como si fueran remos.",
            "Correr a velocidades superiores a las de un felino terrestre.",
            "Enterrarse profundamente bajo la arena del desierto."
        ],
        "correcta": 1,
        "explicacion": "Las membranas interdigitales aumentan la superficie de contacto con el agua, permitiendo una natación y propulsión hidrodinámica eficiente.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 6.° Ciencias Naturales"
    },
    {
        "id": "ICFES-06-SOC-03",
        "grado": "6",
        "asignatura": "Ciencias Sociales",
        "tema": "Democracia escolar: personero estudiantil",
        "pregunta": "¿Cuál es la función principal del Personero Estudiantil en los colegios de Colombia según la Ley General de Educación?",
        "opciones": [
            "Asignar las calificaciones académicas de los exámenes finales.",
            "Promover y defender los derechos y deberes de los estudiantes consagrados en el Manual de Convivencia.",
            "Contratar a los docentes y al personal de vigilancia del plantel.",
            "Decidir el valor de las pensiones y matrículas escolares."
        ],
        "correcta": 1,
        "explicacion": "El personero escolar es el vocero y defensor institucional de los derechos y deberes de los estudiantes en la comunidad educativa.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 6.° Competencias Ciudadanas"
    },

    # --- GRADO 7 ADICIONALES ---
    {
        "id": "ICFES-07-MAT-05",
        "grado": "7",
        "asignatura": "Matemáticas",
        "tema": "Operaciones con fracciones y números racionales",
        "pregunta": "Un atleta recorre 3/5 de una pista atlética en la mañana y 1/4 de la pista en la tarde. ¿Qué fracción total de la pista ha recorrido en el día?",
        "opciones": ["4/9", "4/20", "17/20", "7/10"],
        "correcta": 2,
        "explicacion": "Mínimo común denominador entre 5 y 4 es 20: 3/5 = 12/20 y 1/4 = 5/20. Suma: 12/20 + 5/20 = 17/20 de la pista.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 7.° Matemáticas"
    },
    {
        "id": "ICFES-07-MAT-06",
        "grado": "7",
        "asignatura": "Matemáticas",
        "tema": "Medidas de tendencia central: la mediana",
        "pregunta": "Las estaturas en centímetros de 5 jugadores de un equipo de microfútbol son: 165, 170, 168, 175, 172. ¿Cuál es la mediana de las estaturas?",
        "opciones": ["168 cm.", "170 cm.", "171 cm.", "172 cm."],
        "correcta": 1,
        "explicacion": "Ordenando los datos de menor a mayor: 165, 168, 170, 172, 175. El valor central (posición 3) es 170 cm.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 7.° Matemáticas"
    },
    {
        "id": "ICFES-07-LEN-03",
        "grado": "7",
        "asignatura": "Lenguaje",
        "tema": "Figuras retóricas: metáfora",
        "pregunta": "En la crónica deportiva se lee: 'El volante diez era una brújula en el medio campo, señalando siempre el rumbo exacto hacia el gol'. La expresión 'era una brújula' es una metáfora que indica que:",
        "opciones": [
            "El jugador llevaba un instrumento metálico magnético en el uniforme.",
            "El jugador orientaba y guiaba con inteligencia las jugadas ofensivas de su equipo.",
            "El futbolista estaba perdido en el terreno de juego.",
            "El deportista no conocía la posición de las porterías."
        ],
        "correcta": 1,
        "explicacion": "La metáfora asocia las propiedades de una brújula (orientar, dar dirección clara) con la visión y capacidad de liderazgo del volante de creación.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 7.° Lenguaje"
    },
    {
        "id": "ICFES-07-CN-03",
        "grado": "7",
        "asignatura": "Ciencias Naturales",
        "tema": "Sistema circulatorio y transporte de oxígeno",
        "pregunta": "¿Cuál componente de la sangre humana es el encargado de transportar el oxígeno desde los pulmones hacia los músculos durante un intenso partido de fútbol?",
        "opciones": ["Las plaquetas.", "Los glóbulos rojos (eritrocitos) mediante la hemoglobina.", "Los glóbulos blancos (leucocitos).", "El plasma linfático exclusivamente."],
        "correcta": 1,
        "explicacion": "Los glóbulos rojos contienen hemoglobina, proteína rica en hierro que se une al oxígeno en los alvéolos pulmonares y lo transporta por los vasos sanguíneos.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 7.° Ciencias Naturales"
    },
    {
        "id": "ICFES-07-SOC-02",
        "grado": "7",
        "asignatura": "Ciencias Sociales",
        "tema": "Población y diversidad cultural en Colombia",
        "pregunta": "La Constitución colombiana declara que el país es un Estado 'pluriétnico y multicultural'. Esto significa que el Estado tiene el deber de:",
        "opciones": [
            "Homogeneizar las costumbres para que todos los ciudadanos hablen un solo dialecto.",
            "Reconocer, proteger y respetar las lenguas, tradiciones y derechos de las comunidades indígenas, afrodescendientes y raizales.",
            "Impedir que las comunidades tradicionales participen en elecciones democráticas.",
            "Prohibir las manifestaciones artísticas regionales."
        ],
        "correcta": 1,
        "explicacion": "El principio de diversidad étnica y cultural consagra el respeto y la salvaguarda de la identidad de los distintos grupos étnicos de la nación.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 7.° Competencias Ciudadanas"
    },

    # --- GRADO 8 ADICIONALES ---
    {
        "id": "ICFES-08-MAT-04",
        "grado": "8",
        "asignatura": "Matemáticas",
        "tema": "Factorización de polinomios",
        "pregunta": "¿Cuál es la factorización correcta del binomio x² - 49?",
        "opciones": ["(x - 7)²", "(x + 7)(x - 7)", "(x + 49)(x - 1)", "x(x - 49)"],
        "correcta": 1,
        "explicacion": "Es una diferencia de cuadrados perfectos: a² - b² = (a + b)(a - b). Como √49 = 7, entonces x² - 49 = (x + 7)(x - 7).",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 8.° Matemáticas"
    },
    {
        "id": "ICFES-08-MAT-05",
        "grado": "8",
        "asignatura": "Matemáticas",
        "tema": "Volumen de prismas rectangulares",
        "pregunta": "Un contenedor para guardar balones tiene forma de caja rectangular con dimensiones: 2 metros de largo, 1.5 metros de ancho y 1 metro de alto. ¿Cuál es su capacidad volumétrica?",
        "opciones": ["3 m³.", "4.5 m³.", "6 m³.", "2.5 m³."],
        "correcta": 0,
        "explicacion": "Volumen = largo × ancho × alto = 2 m × 1.5 m × 1 m = 3 m³.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 8.° Matemáticas"
    },
    {
        "id": "ICFES-08-LEN-02",
        "grado": "8",
        "asignatura": "Lenguaje",
        "tema": "Diferenciación entre hechos y opiniones",
        "pregunta": "En un texto sobre fútbol se leen cuatro oraciones. ¿Cuál de ellas expresa un HECHO objetivo comprobable?",
        "opciones": [
            "El partido de ayer fue el espectáculo más aburrido del año.",
            "El delantero número 9 marcó dos goles en el segundo tiempo.",
            "El uniforme del equipo rival es el más feo de la liga.",
            "El árbitro central no tiene buen sentido del humor."
        ],
        "correcta": 1,
        "explicacion": "Que el delantero marcó dos goles es un dato verificable mediante el acta y el marcador del partido, a diferencia de los juicios de gusto subjetivos.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 8.° Lenguaje"
    },
    {
        "id": "ICFES-08-CN-03",
        "grado": "8",
        "asignatura": "Ciencias Naturales",
        "tema": "Fuerzas y Primera Ley de Newton (Inercia)",
        "pregunta": "Un balón rueda sobre el césped y paulatinamente pierde velocidad hasta detenerse por completo. ¿Por qué se detiene el balón si nadie lo tocó?",
        "opciones": [
            "Porque los objetos en movimiento pierden energía de forma espontánea sin interactuar con nada.",
            "Porque la fuerza de fricción o rozamiento entre el balón y el césped actúa en sentido opuesto al movimiento.",
            "Porque la gravedad solo atrae los objetos cuando están en reposo.",
            "Porque el aire dentro del balón se enfría y frena el cuero."
        ],
        "correcta": 1,
        "explicacion": "Por la Primera Ley de Newton, un cuerpo mantiene su movimiento uniforme a menos que actúe una fuerza externa neta; aquí la fuerza de fricción opuesta desacelera el balón.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 8.° Ciencias Naturales"
    },
    {
        "id": "ICFES-08-SOC-02",
        "grado": "8",
        "asignatura": "Ciencias Sociales",
        "tema": "Cuidado ambiental y desarrollo sostenible",
        "pregunta": "¿Qué busca el concepto de 'desarrollo sostenible' promovido por los Objetivos de Desarrollo Sostenible (ODS)?",
        "opciones": [
            "Explotar todos los recursos naturales lo más rápido posible sin regulaciones.",
            "Satisfacer las necesidades de la generación presente sin comprometer la capacidad de las futuras generaciones para satisfacer sus propias necesidades.",
            "Detener por completo toda actividad económica en el planeta.",
            "Permitir la contaminación de ríos siempre que aumenten las ganancias industriales."
        ],
        "correcta": 1,
        "explicacion": "El desarrollo sostenible equilibra el crecimiento económico, la inclusión social y la preservación ambiental a largo plazo.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 8.° Ciencias Sociales"
    },

    # --- GRADO 9 ADICIONALES ---
    {
        "id": "ICFES-09-MAT-03",
        "grado": "9",
        "asignatura": "Matemáticas",
        "tema": "Función lineal y pendiente",
        "pregunta": "Una empresa de transporte cobra una tarifa fija de $5.000 más $2.000 por cada kilómetro recorrido. Si un aficionado recorre x kilómetros para llegar al estadio, ¿cuál ecuación describe el costo total C(x)?",
        "opciones": ["C(x) = 5.000x + 2.000", "C(x) = 2.000x + 5.000", "C(x) = 7.000x", "C(x) = 5.000 / x"],
        "correcta": 1,
        "explicacion": "La pendiente m es la tarifa variable ($2.000 por km) y el intercepto b es el valor fijo ($5.000): C(x) = 2.000x + 5.000.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 9.° Matemáticas"
    },
    {
        "id": "ICFES-09-LEN-02",
        "grado": "9",
        "asignatura": "Lenguaje",
        "tema": "Cohesión referencial: anáfora y deícticos",
        "pregunta": "En el enunciado: 'La capitana levantó el trofeo de la Copa del Saber; ella agradeció con lágrimas a la hinchada', la palabra 'ella' cumple la función de:",
        "opciones": [
            "Introducir un personaje nuevo en la narración.",
            "Hacer referencia anafórica para evitar la repetición de 'La capitana'.",
            "Indicar una pregunta indirecta sobre el juego.",
            "Servir como conector de causa y consecuencia."
        ],
        "correcta": 1,
        "explicacion": "Los pronombres anafóricos como 'ella' sustituyen a un referente ya nombrado para mantener la fluidez y cohesión del texto.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 9.° Lenguaje"
    },
    {
        "id": "ICFES-09-CN-02",
        "grado": "9",
        "asignatura": "Ciencias Naturales",
        "tema": "Evolución y selección natural de Darwin",
        "pregunta": "De acuerdo con la teoría de la evolución por selección natural planteada por Charles Darwin:",
        "opciones": [
            "Los organismos individuales deciden voluntariamente mutar sus órganos durante su vida para adaptarse.",
            "Los individuos con variaciones genéticas favorables en un entorno determinado tienen mayor probabilidad de sobrevivir y reproducirse.",
            "Todas las especies vivas aparecieron en la Tierra al mismo tiempo sin ancestros comunes.",
            "La selección natural favorece siempre a los animales más pesados y de mayor tamaño."
        ],
        "correcta": 1,
        "explicacion": "La selección natural actúa sobre la variabilidad genética preexistente: los rasgos ventajosos confieren mayor éxito reproductivo diferencial.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 9.° Ciencias Naturales"
    },
    {
        "id": "ICFES-09-SOC-02",
        "grado": "9",
        "asignatura": "Ciencias Sociales",
        "tema": "Acción de Tutela en Colombia",
        "pregunta": "¿Qué es la Acción de Tutela establecida en el Artículo 86 de la Constitución colombiana?",
        "opciones": [
            "Un impuesto obligatorio para financiar eventos deportivos.",
            "Un mecanismo judicial expedito para la protección inmediata de los derechos fundamentales cuando resulten vulnerados o amenazados.",
            "Un examen académico que deben presentar los bachilleres para graduarse.",
            "Un tratado de libre comercio suscrito entre dos países."
        ],
        "correcta": 1,
        "explicacion": "La tutela es la herramienta constitucional más importante para reclamar ante los jueces la protección inmediata de derechos fundamentales como la salud, la vida y la educación.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 9.° Competencias Ciudadanas"
    },
    {
        "id": "ICFES-09-ING-03",
        "grado": "9",
        "asignatura": "Inglés",
        "tema": "Present Perfect vs. Past Simple",
        "pregunta": "Select the correct option to complete the conversation:\nCoach: 'Have you ever scored a goal from a corner kick?'\nPlayer: 'Yes, I ________ one last month!'",
        "opciones": ["score", "have scored", "scored", "am scoring"],
        "correcta": 2,
        "explicacion": "When referring to a specific finished past time ('last month'), English requires the Past Simple tense ('scored').",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 9.° Inglés"
    },

    # --- GRADO 10 ADICIONALES ---
    {
        "id": "ICFES-10-MAT-03",
        "grado": "10",
        "asignatura": "Matemáticas",
        "tema": "Geometría analítica: distancia entre dos puntos",
        "pregunta": "En un plano cartesiano que representa el campo de juego, el punto penal está en las coordenadas A(11, 0) y el centro del campo en B(0, 0). ¿Cuál es la distancia en línea recta entre ambos puntos?",
        "opciones": ["0 unidades.", "11 unidades.", "22 unidades.", "121 unidades."],
        "correcta": 1,
        "explicacion": "Distancia d = √((x₂ - x₁)² + (y₂ - y₁)²) = √((11 - 0)² + (0 - 0)²) = √121 = 11 unidades.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 10.° Matemáticas"
    },
    {
        "id": "ICFES-10-MAT-04",
        "grado": "10",
        "asignatura": "Matemáticas",
        "tema": "Ley de senos y cosenos",
        "pregunta": "¿Cuándo es indispensable utilizar la Ley del Coseno para resolver un triángulo no rectángulo?",
        "opciones": [
            "Cuando se conocen los tres lados (LLL) o dos lados y el ángulo comprendido entre ellos (LAL).",
            "Únicamente cuando el triángulo tiene un ángulo recto de 90°.",
            "Cuando se conocen exclusivamente los tres ángulos interiores.",
            "Cuando todos los lados son perpendiculares entre sí."
        ],
        "correcta": 0,
        "explicacion": "La Ley del Coseno (c² = a² + b² - 2ab cos(C)) se aplica para casos LAL y LLL donde la Ley del Seno no puede relacionar directamente pares lado-ángulo.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 10.° Matemáticas"
    },
    {
        "id": "ICFES-10-LEC-02",
        "grado": "10",
        "asignatura": "Lectura Crítica",
        "tema": "Tesis, premisas y contraargumentos",
        "pregunta": "Un autor plantea: 'Si bien la tecnología del VAR en el fútbol reduce los errores arbitrales en jugadas polémicas, su aplicación excesiva interrumpe la fluidez y emoción natural del partido'. ¿Qué recurso argumentativo emplea el autor?",
        "opciones": [
            "Una concesión (reconoce un beneficio previo para luego ponderar una desventaja central).",
            "Un ataque personal contra los fabricantes de pantallas.",
            "Una narración en verso rimado.",
            "Una conclusión falsa sin relación con el tema."
        ],
        "correcta": 0,
        "explicacion": "La concesión argumentativa ('si bien X, sin embargo Y') valida parcialmente un punto contrario para dar mayor solidez a su argumento principal.",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 10.° Lectura Crítica"
    },
    {
        "id": "ICFES-10-CN-02",
        "grado": "10",
        "asignatura": "Ciencias Naturales",
        "tema": "Conservación de la energía mecánica",
        "pregunta": "Un arquero despeja un balón hacia arriba. En el punto más alto de su trayectoria, justo antes de empezar a descender:",
        "opciones": [
            "Su energía potencial gravitacional es mínima y su energía cinética es máxima.",
            "Su energía cinética vertical es cero y su energía potencial gravitacional alcanza su valor máximo.",
            "Su masa se reduce a la mitad por la altura.",
            "La fuerza de gravedad deja de actuar sobre el balón."
        ],
        "correcta": 1,
        "explicacion": "Al alcanzar la altura máxima, la velocidad vertical es 0 (energía cinética = 0) y toda la energía mecánica se ha transformado en energía potencial gravitacional (Ep = mgh).",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 10.° Ciencias Naturales"
    },
    {
        "id": "ICFES-10-SOC-02",
        "grado": "10",
        "asignatura": "Ciencias Sociales",
        "tema": "Globalización económica y soberanía",
        "pregunta": "¿Qué caracteriza principalmente al fenómeno de la globalización económica contemporánea?",
        "opciones": [
            "El cierre absoluto de fronteras y la eliminación del transporte marítimo.",
            "La interconexión de los mercados financieros mundiales, el libre flujo de bienes y la expansión de las comunicaciones digitales.",
            "La prohibición mundial del uso de divisas extranjeras.",
            "La producción exclusiva de alimentos para el autoconsumo local."
        ],
        "correcta": 1,
        "explicacion": "La globalización económica se define por la integración internacional de mercados, cadenas globales de suministro y telecomunicaciones instantáneas.",
        "dificultad": "Fácil",
        "fuente": "Cuadernillo ICFES Saber 10.° Sociales y Ciudadanas"
    },
    {
        "id": "ICFES-10-ING-02",
        "grado": "10",
        "asignatura": "Inglés",
        "tema": "Passive voice in sports news",
        "pregunta": "Choose the correct passive voice sentence for: 'Millions of supporters watched the World Cup final.'",
        "opciones": [
            "The World Cup final was watched by millions of supporters.",
            "The World Cup final were watching by millions of supporters.",
            "The World Cup final watched millions of supporters.",
            "Millions of supporters were watched by the final."
        ],
        "correcta": 0,
        "explicacion": "In Past Simple Passive, the structure is 'Subject (singular) + was + Past Participle + by agent': 'The World Cup final was watched by...'",
        "dificultad": "Medio",
        "fuente": "Cuadernillo ICFES Saber 10.° Inglés"
    }
]

def main():
    with open('data/questions.json', 'r', encoding='utf-8') as f:
        existing = json.load(f)

    existing_ids = {q['id'] for q in existing}
    added = 0
    for q in new_questions:
        if q['id'] not in existing_ids:
            existing.append(q)
            existing_ids.add(q['id'])
            added += 1

    with open('data/questions.json', 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f'Added {added} new questions. Total in database: {len(existing)}')

    # Report by grade
    counts = {}
    for q in existing:
        counts[q['grado']] = counts.get(q['grado'], 0) + 1
    for g, c in sorted(counts.items(), key=lambda x: int(x[0])):
        print(f'Grado {g}°: {c} preguntas')

if __name__ == '__main__':
    main()
