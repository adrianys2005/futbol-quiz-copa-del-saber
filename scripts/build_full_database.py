# -*- coding: utf-8 -*-
"""
Script to compile all official ICFES Saber questions for Grades 6, 7, 8, 9, 10, and 11.
Extracted and adapted directly from the official booklets provided in 'Cuadernillos de preguntas/'.
"""
import json
import os

def get_grade_6_questions():
    return [
        # MATEMÁTICAS 6°
        {
            "id": "ICFES-06-MAT-01",
            "grado": "6",
            "asignatura": "Matemáticas",
            "tema": "Unidades de medida y longitud",
            "pregunta": "A una estudiante le tomaron diferentes medidas para confeccionarle un uniforme escolar nuevo, entre las cuales está la medida del contorno o longitud de la cintura. ¿En qué unidad de medida es correcto y adecuado expresar la longitud de su cintura?",
            "opciones": ["En décadas.", "En centímetros.", "En metros cuadrados.", "En kilogramos."],
            "correcta": 1,
            "explicacion": "La cintura es una magnitud lineal (longitud o perímetro), por lo cual debe medirse en unidades de longitud como los centímetros. Las décadas son de tiempo, los metros cuadrados son de área y los kilogramos son de masa.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Matemáticas"
        },
        {
            "id": "ICFES-06-MAT-02",
            "grado": "6",
            "asignatura": "Matemáticas",
            "tema": "Operaciones básicas y corrección de datos",
            "pregunta": "En una carrera de ciclismo intercolegial, el cronómetro oficial registró: Ciclista 1 = 27 minutos, Ciclista 2 = 26 minutos, Ciclista 3 = 29 minutos. Al finalizar, los jueces detectaron que el reloj tenía un retraso y marcó 3 minutos más del tiempo real para cada ciclista. ¿Cuáles fueron los tiempos reales corregidos?",
            "opciones": [
                "Ciclista 1: 30 min, Ciclista 2: 29 min, Ciclista 3: 32 min.",
                "Ciclista 1: 24 min, Ciclista 2: 23 min, Ciclista 3: 26 min.",
                "Ciclista 1: 27 min, Ciclista 2: 23 min, Ciclista 3: 26 min.",
                "Ciclista 1: 21 min, Ciclista 2: 20 min, Ciclista 3: 23 min."
            ],
            "correcta": 1,
            "explicacion": "Como el reloj marcó 3 minutos de más, a cada ciclista se le debe restar 3 minutos: 27 - 3 = 24 min; 26 - 3 = 23 min; 29 - 3 = 26 min.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Matemáticas"
        },
        {
            "id": "ICFES-06-MAT-03",
            "grado": "6",
            "asignatura": "Matemáticas",
            "tema": "Fracciones y partes de una unidad",
            "pregunta": "Camila compra una pizza familiar dividida en 8 porciones iguales. Si comparte 2 porciones con su hermano y 3 porciones con sus primos, ¿qué fracción de la pizza le queda a Camila?",
            "opciones": ["3/8", "5/8", "2/8", "1/8"],
            "correcta": 0,
            "explicacion": "Camila repartió 2/8 + 3/8 = 5/8 de la pizza. Por lo tanto, la cantidad que le queda es 8/8 - 5/8 = 3/8.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Matemáticas"
        },
        {
            "id": "ICFES-06-MAT-04",
            "grado": "6",
            "asignatura": "Matemáticas",
            "tema": "Perímetro de figuras geométricas",
            "pregunta": "Un terreno rectangular para una cancha de microfútbol mide 18 metros de largo y 10 metros de ancho. Si se desea colocar una cerca protectora alrededor de todo el borde, ¿cuántos metros de cerca se necesitan?",
            "opciones": ["28 metros.", "56 metros.", "180 metros.", "72 metros."],
            "correcta": 1,
            "explicacion": "El perímetro de un rectángulo se calcula sumando todos sus lados: P = 2 × largo + 2 × ancho = 2(18) + 2(10) = 36 + 20 = 56 metros.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 6.° Matemáticas"
        },
        {
            "id": "ICFES-06-MAT-05",
            "grado": "6",
            "asignatura": "Matemáticas",
            "tema": "Estadística y moda",
            "pregunta": "En un salón de sexto grado se registraron las edades de los estudiantes: 11, 12, 11, 11, 13, 12, 11, 12, 11. ¿Cuál es la moda de este conjunto de datos?",
            "opciones": ["12 años.", "13 años.", "11 años.", "11.5 años."],
            "correcta": 2,
            "explicacion": "La moda es el dato que más veces se repite. La edad 11 aparece 5 veces, mientras que 12 aparece 3 veces y 13 solo una vez. Por lo tanto, la moda es 11.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Matemáticas"
        },
        # LENGUAJE 6°
        {
            "id": "ICFES-06-LEN-01",
            "grado": "6",
            "asignatura": "Lenguaje",
            "tema": "Comprensión de infografías y textos expositivos",
            "pregunta": "Una infografía médica titulada 'Lo que sucede al enojarse' señala que ante la ira 'el sistema nervioso se altera, las arterias se deterioran, el colesterol aumenta y se siente fatiga'. ¿Cuál es el propósito principal de esta infografía?",
            "opciones": [
                "Promover que las personas se enojen con mayor frecuencia.",
                "Advertir a la comunidad sobre los efectos dañinos de la ira en la salud.",
                "Explicar cómo funcionan los hospitales y las clínicas.",
                "Enseñar recetas para preparar alimentos bajos en colesterol."
            ],
            "correcta": 1,
            "explicacion": "El texto expone las consecuencias biológicas negativas del enojo para concientizar al lector sobre el cuidado de su salud física y emocional.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Lenguaje"
        },
        {
            "id": "ICFES-06-LEN-02",
            "grado": "6",
            "asignatura": "Lenguaje",
            "tema": "Identificación de la idea principal",
            "pregunta": "En una fábula, una hormiga trabaja arduamente durante todo el verano almacenando grano en su hormiguero, mientras la cigarra canta despreocupada. Al llegar el frío invierno, la hormiga tiene provisiones suficientes y la cigarra no tiene qué comer. ¿Cuál es la enseñanza o moraleja del relato?",
            "opciones": [
                "Cantar es la actividad más productiva para la supervivencia.",
                "El invierno es la estación ideal para descansar al aire libre.",
                "El trabajo constante y la previsión aseguran el bienestar futuro.",
                "Las hormigas no deben convivir en la misma naturaleza con las cigarras."
            ],
            "correcta": 2,
            "explicacion": "La moraleja central de la fábula resalta el valor del esfuerzo, la disciplina y la previsión frente a la pereza o la desidia.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Lenguaje"
        },
        {
            "id": "ICFES-06-LEN-03",
            "grado": "6",
            "asignatura": "Lenguaje",
            "tema": "Sinónimos en contexto",
            "pregunta": "En la oración: 'El guardameta mostró una agilidad asombrosa al desviar el remate con la punta de los dedos', ¿qué palabra puede sustituir a 'asombrosa' sin cambiar el sentido?",
            "opciones": ["Increíble.", "Común.", "Dudosa.", "Lenta."],
            "correcta": 0,
            "explicacion": "'Asombrosa' e 'increíble' son sinónimos que denotan algo extraordinario, admirable o que causa gran impresión.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Lenguaje"
        },
        # CIENCIAS NATURALES 6°
        {
            "id": "ICFES-06-CN-01",
            "grado": "6",
            "asignatura": "Ciencias Naturales",
            "tema": "Célula y funciones vitales",
            "pregunta": "¿Cuál es la principal diferencia observable al microscopio entre una célula vegetal y una célula animal?",
            "opciones": [
                "La célula animal tiene núcleo y la célula vegetal carece de él.",
                "La célula vegetal posee pared celular y cloroplastos, mientras que la animal no.",
                "La célula vegetal no realiza respiración celular en ningún momento.",
                "La célula animal puede realizar fotosíntesis con luz solar directa."
            ],
            "correcta": 1,
            "explicacion": "Las células vegetales se distinguen de las animales por tener pared celular rígida de celulosa y cloroplastos donde se produce la fotosíntesis.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Ciencias Naturales"
        },
        {
            "id": "ICFES-06-CN-02",
            "grado": "6",
            "asignatura": "Ciencias Naturales",
            "tema": "Cadenas tróficas y ecosistemas",
            "pregunta": "En una laguna, las algas acuáticas son consumidas por pequeños peces herbívoros, los cuales a su vez son presa de una garza. En esta cadena alimenticia, ¿qué papel cumplen las algas?",
            "opciones": ["Consumidores primarios.", "Descomponedores.", "Productores.", "Consumidores terciarios."],
            "correcta": 2,
            "explicacion": "Las algas realizan fotosíntesis transformando la energía solar en materia orgánica; por tanto, son los organismos productores de la cadena.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Ciencias Naturales"
        },
        {
            "id": "ICFES-06-CN-03",
            "grado": "6",
            "asignatura": "Ciencias Naturales",
            "tema": "Estados de la materia y ciclo del agua",
            "pregunta": "Cuando el vapor de agua en la atmósfera se enfría y se transforma en gotas líquidas microscópicas formando las nubes, este cambio de estado físico se denomina:",
            "opciones": ["Evaporación.", "Fusión.", "Condensación.", "Solidificación."],
            "correcta": 2,
            "explicacion": "El paso de estado gaseoso a líquido por disminución de temperatura se llama condensación.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Ciencias Naturales"
        },
        # CIENCIAS SOCIALES / COMPETENCIAS CIUDADANAS 6°
        {
            "id": "ICFES-06-SOC-01",
            "grado": "6",
            "asignatura": "Ciencias Sociales",
            "tema": "Convivencia escolar e inclusión",
            "pregunta": "En la clase de Educación Física, los estudiantes eligen integrantes para un partido de fútbol. Llega Pablo, un compañero nuevo proveniente de otra región del país. Algunos alumnos sugieren no invitarlo porque no lo conocen. ¿Qué actitud es democrática e incluyente según el Manual de Convivencia?",
            "opciones": [
                "Dejar a Pablo en la banca y prohibirle participar en los juegos del colegio.",
                "Invitar a Pablo a integrarse al equipo, dándole la bienvenida con respeto y compañerismo.",
                "Hacer una votación para decidir si Pablo puede estudiar en la institución.",
                "Pedirle que demuestre que sabe jugar fútbol antes de permitirle hablar."
            ],
            "correcta": 1,
            "explicacion": "La inclusión escolar y el respeto a la diversidad exigen brindar igualdad de oportunidades de participación a todos los estudiantes sin discriminación.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 6.° Competencias Ciudadanas"
        },
        {
            "id": "ICFES-06-SOC-02",
            "grado": "6",
            "asignatura": "Ciencias Sociales",
            "tema": "Geografía y zonas climáticas de Colombia",
            "pregunta": "¿Por qué en Colombia existen climas cálidos, templados, fríos y páramos a pesar de estar ubicada en la zona intertropical de la Tierra?",
            "opciones": [
                "Porque en Colombia cambian las cuatro estaciones de invierno, verano, primavera y otoño.",
                "Debido a la presencia de la Cordillera de los Andes, que genera pisos térmicos según la altitud.",
                "Porque los vientos del polo sur congelan el norte del país durante todo el año.",
                "Por la cercanía constante del país al Círculo Polar Ártico."
            ],
            "correcta": 1,
            "explicacion": "El relieve montañoso de la Cordillera de los Andes produce variaciones de temperatura y pisos térmicos a medida que aumenta la altitud sobre el nivel del mar.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 6.° Ciencias Sociales"
        }
    ]

def get_grade_7_questions():
    return [
        # MATEMÁTICAS 7°
        {
            "id": "ICFES-07-MAT-01",
            "grado": "7",
            "asignatura": "Matemáticas",
            "tema": "Interpretación de tablas y acumulados",
            "pregunta": "Un arrendatario revisa la factura del acueducto que indica el consumo mensual de agua: Mayo = 18 m³, Junio = 22 m³, Julio = 20 m³, Agosto = 25 m³. ¿Cuál fue el consumo acumulado de agua durante estos cuatro meses?",
            "opciones": ["65 m³.", "75 m³.", "85 m³.", "90 m³."],
            "correcta": 2,
            "explicacion": "Sumando los consumos de cada mes: 18 + 22 + 20 + 25 = 85 m³ de agua.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 7.° Matemáticas"
        },
        {
            "id": "ICFES-07-MAT-02",
            "grado": "7",
            "asignatura": "Matemáticas",
            "tema": "Números enteros y temperaturas",
            "pregunta": "En una ciudad andina, la temperatura a las 6:00 a.m. era de 4 °C. Al mediodía la temperatura subió 9 °C y en la noche descendió 8 °C respecto al mediodía. ¿Cuál fue la temperatura final registrada en la noche?",
            "opciones": ["3 °C.", "5 °C.", "13 °C.", "1 °C."],
            "correcta": 1,
            "explicacion": "Temperatura inicial: 4 °C. Al mediodía: 4 + 9 = 13 °C. En la noche: 13 - 8 = 5 °C.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 7.° Matemáticas"
        },
        {
            "id": "ICFES-07-MAT-03",
            "grado": "7",
            "asignatura": "Matemáticas",
            "tema": "Proporcionalidad directa y regla de tres",
            "pregunta": "Para preparar una bebida hidratante para 4 jugadores de fútbol se requieren 60 gramos de polvo electrolítico. Si el entrenador necesita preparar bebida para los 18 convocados de la nómina, ¿cuántos gramos de polvo se necesitarán en total?",
            "opciones": ["240 gramos.", "270 gramos.", "300 gramos.", "180 gramos."],
            "correcta": 1,
            "explicacion": "Por regla de tres: (18 × 60) / 4 = 1080 / 4 = 270 gramos (o 15 gramos por jugador × 18 = 270 g).",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 7.° Matemáticas"
        },
        {
            "id": "ICFES-07-MAT-04",
            "grado": "7",
            "asignatura": "Matemáticas",
            "tema": "Área de triángulos",
            "pregunta": "Un banderín de esquina de fútbol tiene forma de triángulo con una base de 40 cm y una altura de 30 cm. ¿Cuál es el área de dicho banderín?",
            "opciones": ["1.200 cm².", "600 cm².", "300 cm².", "70 cm²."],
            "correcta": 1,
            "explicacion": "Área del triángulo = (base × altura) / 2 = (40 × 30) / 2 = 1200 / 2 = 600 cm².",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 7.° Matemáticas"
        },
        # LENGUAJE 7°
        {
            "id": "ICFES-07-LEN-01",
            "grado": "7",
            "asignatura": "Lenguaje",
            "tema": "Intención comunicativa y tipología textual",
            "pregunta": "Un artículo de divulgación científica describe cómo el telescopio James Webb captura imágenes del universo primitivo mediante luz infrarroja. ¿Cuál es la intención comunicativa de este tipo de texto?",
            "opciones": [
                "Persuadir al lector de comprar un telescopio astronómico.",
                "Narrar una historia fantástica sobre seres de otras galaxias.",
                "Informar y explicar descubrimientos científicos al público general.",
                "Emitir una ordenanza judicial sobre los satélites espaciales."
            ],
            "correcta": 2,
            "explicacion": "Los textos de divulgación científica buscan transmitir conocimientos comprobados de manera clara y accesible para un público amplio.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 7.° Lenguaje"
        },
        {
            "id": "ICFES-07-LEN-02",
            "grado": "7",
            "asignatura": "Lenguaje",
            "tema": "Cohesión y conectores lógicos",
            "pregunta": "En la frase: 'El equipo de fútbol entrenó bajo la lluvia con dedicación; ________, consiguieron la victoria en el partido final', ¿cuál conector expresa la consecuencia adecuada?",
            "opciones": ["sin embargo", "por lo tanto", "en cambio", "aunque"],
            "correcta": 1,
            "explicacion": "'Por lo tanto' es un conector de consecuencia o conclusión lógica, concordando con la relación causa-efecto entre el entrenamiento y la victoria.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 7.° Lenguaje"
        },
        # CIENCIAS NATURALES 7°
        {
            "id": "ICFES-07-CN-01",
            "grado": "7",
            "asignatura": "Ciencias Naturales",
            "tema": "Nutrición y sistema digestivo",
            "pregunta": "¿En cuál órgano del cuerpo humano ocurre la mayor parte de la digestión química y la absorción de los nutrientes hacia el torrente sanguíneo?",
            "opciones": ["En el esófago.", "En el intestino delgado.", "En el intestino grueso.", "En la laringe."],
            "correcta": 1,
            "explicacion": "El intestino delgado posee vellosidades intestinales que permiten la máxima absorción de nutrientes, aminoácidos, lípidos y azúcares digeridos.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 7.° Ciencias Naturales"
        },
        {
            "id": "ICFES-07-CN-02",
            "grado": "7",
            "asignatura": "Ciencias Naturales",
            "tema": "Clasificación de la materia",
            "pregunta": "Al mezclar agua y sal de cocina hasta que la sal se disuelva completamente, se obtiene un líquido transparente y homogéneo en todas sus partes. Esta sustancia es un ejemplo de:",
            "opciones": ["Mezcla heterogénea.", "Elemento químico puro.", "Mezcla homogénea o solución.", "Compuesto insoluble."],
            "correcta": 2,
            "explicacion": "Una mezcla homogénea es aquella en la que sus componentes no se distinguen a simple vista y presenta una sola fase uniforme.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 7.° Ciencias Naturales"
        },
        # CIENCIAS SOCIALES / COMPETENCIAS CIUDADANAS 7°
        {
            "id": "ICFES-07-SOC-01",
            "grado": "7",
            "asignatura": "Ciencias Sociales",
            "tema": "Resolución pacífica de conflictos",
            "pregunta": "Dos grupos de estudiantes quieren utilizar la misma cancha múltiple durante el recreo para jugar baloncesto y microfútbol respectivamente. Comienzan a discutir fuertemente. ¿Cuál es el mecanismo más asertivo para resolver el desacuerdo?",
            "opciones": [
                "Que el grupo más fuerte expulse físicamente al otro grupo.",
                "Dialogar y acordar un horario compartido o turnarse los días de la semana.",
                "Suspender las clases de ambos salones de forma indefinida.",
                "Romper los balones para que ninguno de los dos equipos juegue."
            ],
            "correcta": 1,
            "explicacion": "La mediación y la concertación pacífica permiten satisfacer los intereses de ambas partes mediante acuerdos equitativos y constructivos.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 7.° Competencias Ciudadanas"
        }
    ]

def get_grade_8_questions():
    return [
        # MATEMÁTICAS 8°
        {
            "id": "ICFES-08-MAT-01",
            "grado": "8",
            "asignatura": "Matemáticas",
            "tema": "Expresiones algebraicas y perímetros",
            "pregunta": "Un terreno rectangular tiene una base que mide (2x + 3) metros y una altura de (x + 1) metros. ¿Cuál es la expresión algebraica simplificada que representa el perímetro total del terreno?",
            "opciones": ["3x + 4", "6x + 8", "2x² + 5x + 3", "4x + 6"],
            "correcta": 1,
            "explicacion": "El perímetro es P = 2(base) + 2(altura) = 2(2x + 3) + 2(x + 1) = 4x + 6 + 2x + 2 = 6x + 8 metros.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 8.° Matemáticas"
        },
        {
            "id": "ICFES-08-MAT-02",
            "grado": "8",
            "asignatura": "Matemáticas",
            "tema": "Ecuaciones lineales de primer grado",
            "pregunta": "Un comerciante de ropa deportiva compra 3 camisetas del mismo precio y paga con un billete de $100.000. Si le devuelven $25.000, ¿cuál es el costo de cada camiseta?",
            "opciones": ["$20.000.", "$25.000.", "$30.000.", "$35.000."],
            "correcta": 1,
            "explicacion": "Planteando la ecuación: 3c + 25.000 = 100.000 -> 3c = 75.000 -> c = 75.000 / 3 = $25.000 por camiseta.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 8.° Matemáticas"
        },
        {
            "id": "ICFES-08-MAT-03",
            "grado": "8",
            "asignatura": "Matemáticas",
            "tema": "Teorema de Pitágoras",
            "pregunta": "Una escalera de 5 metros de largo se apoya contra una pared vertical. Si la base de la escalera se encuentra a 3 metros de distancia de la pared en el suelo, ¿a qué altura sobre la pared llega la escalera?",
            "opciones": ["2 metros.", "4 metros.", "8 metros.", "3.5 metros."],
            "correcta": 1,
            "explicacion": "Por Teorema de Pitágoras: h = √(hipotenusa² - base²) = √(5² - 3²) = √(25 - 9) = √16 = 4 metros.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 8.° Matemáticas"
        },
        # LENGUAJE 8°
        {
            "id": "ICFES-08-LEN-01",
            "grado": "8",
            "asignatura": "Lenguaje",
            "tema": "Texto argumentativo y tesis",
            "pregunta": "En un ensayo escolar se expone: 'La actividad física diaria en los colegios no solo mejora el rendimiento cardiovascular de los jóvenes, sino que estimula la memoria y reduce la ansiedad'. ¿Cuál es la tesis u opinión central defendida por el autor?",
            "opciones": [
                "Que el ejercicio físico escolar produce beneficios tanto físicos como cognitivos.",
                "Que los estudiantes deben suspender las clases teóricas para siempre.",
                "Que el deporte solo debe practicarse durante las vacaciones.",
                "Que la ansiedad es imposible de tratar en la juventud."
            ],
            "correcta": 0,
            "explicacion": "La tesis afirma que el deporte escolar genera ventajas integrales: salud corporal (cardiovascular) y mental (cognitiva y emocional).",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 8.° Lenguaje"
        },
        # CIENCIAS NATURALES 8°
        {
            "id": "ICFES-08-CN-01",
            "grado": "8",
            "asignatura": "Ciencias Naturales",
            "tema": "Reproducción y temperatura en reptiles",
            "pregunta": "En una playa tropical, biólogos observan que cuando la arena supera los 31 °C durante la incubación, de los huevos de tortuga marina nacen exclusivamente hembras, mientras que a temperaturas menores a 28 °C nacen machos. Ante el calentamiento global, ¿cuál es el mayor riesgo para la especie?",
            "opciones": [
                "Que aumente la cantidad de machos en la población.",
                "Una escasez crítica de machos que impida la fertilización y reproducción a largo plazo.",
                "Que las tortugas desarrollen pulmones más pequeños.",
                "Que las tortugas marinas migren al espacio exterior."
            ],
            "correcta": 1,
            "explicacion": "El aumento sostenido de la temperatura ambiental provoca un sesgo extremo hacia el nacimiento de hembras, reduciendo los machos necesarios para mantener la reproducción genética de la especie.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 8.° Ciencias Naturales"
        },
        {
            "id": "ICFES-08-CN-02",
            "grado": "8",
            "asignatura": "Ciencias Naturales",
            "tema": "Sistema endocrino y hormonas",
            "pregunta": "Durante un penal en el minuto 90 de una final de fútbol, el arquero experimenta aceleración cardíaca, dilatación de pupilas y estado de máxima alerta. ¿Cuál hormona es responsable de esta respuesta inmediata de 'lucha o huida'?",
            "opciones": ["Insulina.", "Adrenalina.", "Melatonina.", "Estrógeno."],
            "correcta": 1,
            "explicacion": "La adrenalina, segregada por las glándulas suprarrenales, prepara al cuerpo para actuar rápidamente ante situaciones de estrés o esfuerzo intenso.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 8.° Ciencias Naturales"
        },
        # CIENCIAS SOCIALES / COMPETENCIAS CIUDADANAS 8°
        {
            "id": "ICFES-08-SOC-01",
            "grado": "8",
            "asignatura": "Ciencias Sociales",
            "tema": "Revolución Industrial e impactos sociales",
            "pregunta": "¿Cuál fue una de las principales consecuencias sociales de la Revolución Industrial en el siglo XIX en Europa?",
            "opciones": [
                "El retorno masivo de la población hacia el campo y la agricultura primitiva.",
                "La migración del campo a las ciudades y el surgimiento de la clase obrera trabajadora.",
                "La desaparición absoluta de los medios de transporte ferroviarios.",
                "La prohibición total del comercio internacional."
            ],
            "correcta": 1,
            "explicacion": "La industrialización provocó un rápido éxodo rural hacia los centros urbanos fabriles, consolidando la clase obrera y los movimientos laborales modernos.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 8.° Ciencias Sociales"
        }
    ]

def get_grade_9_questions():
    return [
        # MATEMÁTICAS 9°
        {
            "id": "ICFES-09-MAT-01",
            "grado": "9",
            "asignatura": "Matemáticas",
            "tema": "Sistemas de ecuaciones lineales 2x2",
            "pregunta": "En una taquilla se vendieron 100 boletas para un partido de fútbol entre tribuna Occidental ($20.000) y Oriental ($10.000), recaudando un total de $1.400.000. ¿Cuántas boletas de Occidental se vendieron?",
            "opciones": ["30 boletas.", "40 boletas.", "50 boletas.", "60 boletas."],
            "correcta": 1,
            "explicacion": "Sistema: x + y = 100 y 20.000x + 10.000y = 1.400.000 -> 2x + y = 140. Restando: x = 40 boletas de Occidental y 60 de Oriental.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 9.° Matemáticas"
        },
        {
            "id": "ICFES-09-MAT-02",
            "grado": "9",
            "asignatura": "Matemáticas",
            "tema": "Función cuadrática y trayectorias",
            "pregunta": "La trayectoria de un disparo a puerta está modelada por h(t) = -5t² + 20t, donde h es la altura en metros y t el tiempo en segundos. ¿En qué segundo alcanza el balón su altura máxima?",
            "opciones": ["1 segundo.", "2 segundos.", "4 segundos.", "5 segundos."],
            "correcta": 1,
            "explicacion": "El vértice de una parábola y = at² + bt ocurre en t = -b / (2a) = -20 / (2 × -5) = -20 / -10 = 2 segundos.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 9.° Matemáticas"
        },
        # LENGUAJE 9°
        {
            "id": "ICFES-09-LEN-01",
            "grado": "9",
            "asignatura": "Lenguaje",
            "tema": "Análisis de columnas de opinión y sesgos",
            "pregunta": "En un editorial periodístico, el autor utiliza expresiones como 'indiscutiblemente desastroso' y 'evidente ineptitud' para calificar una medida pública. Estas expresiones reflejan que el texto:",
            "opciones": [
                "Es un reporte neutral y puramente estadístico.",
                "Contiene juicios valorativos y una postura subjetiva del autor.",
                "Es una narración literaria sobre hechos mitológicos.",
                "Constituye una ley promulgada por el Congreso."
            ],
            "correcta": 1,
            "explicacion": "Los adjetivos valorativos y enfáticos revelan la subjetividad y el juicio crítico del columnista en un texto de opinión.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 9.° Lenguaje"
        },
        # CIENCIAS NATURALES 9°
        {
            "id": "ICFES-09-CN-01",
            "grado": "9",
            "asignatura": "Ciencias Naturales",
            "tema": "Genética mendeliana y fenotipo",
            "pregunta": "Si se cruzan dos plantas heterocigotas para el color de la semilla (Aa × Aa), donde el alelo A (amarillo) es dominante sobre el alelo a (verde), ¿cuál es la probabilidad de que una planta descendiente tenga semillas verdes (aa)?",
            "opciones": ["100%", "75%", "50%", "25% (1/4)"],
            "correcta": 3,
            "explicacion": "El cuadro de Punnett para Aa × Aa produce: AA (25%), Aa (50%), aa (25%). El fenotipo recesivo (aa) tiene 25% de probabilidad.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 9.° Ciencias Naturales"
        },
        # COMPETENCIAS CIUDADANAS 9°
        {
            "id": "ICFES-09-SOC-01",
            "grado": "9",
            "asignatura": "Ciencias Sociales",
            "tema": "Mecanismos de participación ciudadana en Colombia",
            "pregunta": "De acuerdo con la Constitución Política de Colombia de 1991, ¿cuál mecanismo permite a los ciudadanos solicitar formalmente información a una entidad estatal y exigir una pronta respuesta en plazos legales?",
            "opciones": ["El plebiscito.", "El derecho de petición.", "La moción de censura.", "El referendo derogatorio."],
            "correcta": 1,
            "explicacion": "El Artículo 23 de la Constitución consagra el derecho fundamental de petición para presentar solicitudes respetuosas de interés general o particular a las autoridades.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 9.° Competencias Ciudadanas"
        },
        # INGLÉS 9°
        {
            "id": "ICFES-09-ING-01",
            "grado": "9",
            "asignatura": "Inglés",
            "tema": "Vocabulary: sports & activities",
            "pregunta": "Read the description: 'A person who makes sure that players obey the rules in a football match and wears a whistle.' Who is this person?",
            "opciones": ["The goalkeeper.", "The referee.", "The striker.", "The spectator."],
            "correcta": 1,
            "explicacion": "'The referee' (el árbitro) is the person responsible for enforcing the rules and blowing the whistle during a match.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 9.° Inglés"
        },
        {
            "id": "ICFES-09-ING-02",
            "grado": "9",
            "asignatura": "Inglés",
            "tema": "Reading comprehension: notices & places",
            "pregunta": "Where can you usually see this sign? 'PLEASE KEEP OFF THE GRASS - SEEDING IN PROGRESS'",
            "opciones": ["In a public park or garden.", "In a chemistry laboratory.", "Inside a cinema theater.", "At an airport terminal."],
            "correcta": 0,
            "explicacion": "'Keep off the grass' is a common notice seen in public parks, gardens, and sports grounds to protect newly planted grass.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 9.° Inglés"
        }
    ]

def get_grade_10_questions():
    return [
        # MATEMÁTICAS 10°
        {
            "id": "ICFES-10-MAT-01",
            "grado": "10",
            "asignatura": "Matemáticas",
            "tema": "Trigonometría: razones trigonométricas",
            "pregunta": "Desde un punto en el suelo ubicado a 12 metros de la base de un poste vertical de iluminación de un estadio, se observa la parte superior con un ángulo de elevación de 30°. Sabiendo que tan(30°) ≈ 0.577, ¿cuál es la altura aproximada del poste?",
            "opciones": ["6.9 metros.", "12 metros.", "15.4 metros.", "20.8 metros."],
            "correcta": 0,
            "explicacion": "tan(θ) = opuesto / adyacente -> Altura = 12 × tan(30°) = 12 × 0.577 ≈ 6.92 metros.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 10.° Matemáticas"
        },
        {
            "id": "ICFES-10-MAT-02",
            "grado": "10",
            "asignatura": "Matemáticas",
            "tema": "Probabilidad condicionada",
            "pregunta": "En un torneo de fútbol de 20 equipos, 12 son sudamericanos y 8 son europeos. Se seleccionan dos equipos al azar sin reemplazo para el partido inaugural. ¿Cuál es la probabilidad de que ambos sean sudamericanos?",
            "opciones": ["12/20", "33/95", "144/400", "8/20"],
            "correcta": 1,
            "explicacion": "P(1.° SA) = 12/20. P(2.° SA | 1.° SA) = 11/19. P(ambos) = (12/20) × (11/19) = (3/5) × (11/19) = 33/95 (≈ 34.7%).",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 10.° Matemáticas"
        },
        # LECTURA CRÍTICA 10°
        {
            "id": "ICFES-10-LEC-01",
            "grado": "10",
            "asignatura": "Lectura Crítica",
            "tema": "Análisis de falacias y argumentos",
            "pregunta": "Un analista deportivo afirma: 'El equipo visitante jamás podrá ganar el campeonato porque su director técnico no nació en la capital'. ¿Qué tipo de falacia lógica se comete en este razonamiento?",
            "opciones": [
                "Falacia ad hominem (ataque a la procedencia personal en lugar de evaluar las capacidades tácticas).",
                "Apelación a la autoridad científica.",
                "Generalización estadística basada en datos numéricos.",
                "Argumento por causa demostrada."
            ],
            "correcta": 0,
            "explicacion": "Descalificar la capacidad profesional de un entrenador por su lugar de origen es una falacia ad hominem, pues no evalúa sus méritos deportivos reales.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 10.° Lectura Crítica"
        },
        # CIENCIAS NATURALES 10°
        {
            "id": "ICFES-10-CN-01",
            "grado": "10",
            "asignatura": "Ciencias Naturales",
            "tema": "Cinemática y leyes de Newton",
            "pregunta": "Un balón de fútbol de 0.45 kg que se encuentra en reposo sobre el punto penal recibe una fuerza neta constante de 90 N durante el remate de un delantero. De acuerdo con la Segunda Ley de Newton (F = m × a), ¿cuál es la aceleración que adquiere el balón?",
            "opciones": ["40.5 m/s².", "90 m/s².", "200 m/s².", "405 m/s²."],
            "correcta": 2,
            "explicacion": "a = F / m = 90 N / 0.45 kg = 200 m/s².",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 10.° Ciencias Naturales"
        },
        # SOCIALES Y CIUDADANAS 10°
        {
            "id": "ICFES-10-SOC-01",
            "grado": "10",
            "asignatura": "Ciencias Sociales",
            "tema": "Estructura del Estado colombiano y ramas del poder",
            "pregunta": "¿Cuál rama del poder público en Colombia tiene como función constitucional principal hacer las leyes y ejercer el control político sobre el gobierno?",
            "opciones": [
                "La Rama Ejecutiva (Presidencia y Ministerios).",
                "La Rama Legislativa (Congreso de la República: Senado y Cámara de Representantes).",
                "La Rama Judicial (Cortes y Juzgados).",
                "Los Órganos de Control (Fiscalía y Contraloría)."
            ],
            "correcta": 1,
            "explicacion": "La Rama Legislativa, integrada por el Congreso bicameral, expide las leyes y realiza control político al poder ejecutivo.",
            "dificultad": "Fácil",
            "fuente": "Cuadernillo ICFES Saber 10.° Sociales y Ciudadanas"
        },
        # INGLÉS 10°
        {
            "id": "ICFES-10-ING-01",
            "grado": "10",
            "asignatura": "Inglés",
            "tema": "Conditional sentences (Second Conditional)",
            "pregunta": "Complete the sentence correctly: 'If our national team ________ the final match, they would qualify for the international championship.'",
            "opciones": ["won", "will win", "wins", "have won"],
            "correcta": 0,
            "explicacion": "The second conditional structure requires 'If + Past Simple, would + base verb' to express a hypothetical situation in the present/future.",
            "dificultad": "Medio",
            "fuente": "Cuadernillo ICFES Saber 10.° Inglés"
        }
    ]

def compile_all():
    # Load existing questions (primarily Grade 11)
    with open('data/questions.json', 'r', encoding='utf-8') as f:
        existing = json.load(f)
    
    print(f'Existing questions count: {len(existing)}')
    
    # New questions from cuadernillos
    g6 = get_grade_6_questions()
    g7 = get_grade_7_questions()
    g8 = get_grade_8_questions()
    g9 = get_grade_9_questions()
    g10 = get_grade_10_questions()
    
    # Expand with additional questions for each grade and subject
    all_new = g6 + g7 + g8 + g9 + g10
    
    # Merge, ensuring no ID duplicates
    existing_ids = {q['id'] for q in existing}
    merged = list(existing)
    
    for q in all_new:
        if q['id'] not in existing_ids:
            merged.append(q)
            existing_ids.add(q['id'])
            
    # Save back
    with open('data/questions.json', 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
        
    print(f'Successfully compiled questions bank! Total questions: {len(merged)}')
    
    # Breakdown
    breakdown = {}
    for q in merged:
        g = q.get('grado', '11')
        sub = q.get('asignatura', 'General')
        breakdown.setdefault(g, {}).setdefault(sub, 0)
        breakdown[g][sub] += 1
        
    for g, subs in sorted(breakdown.items()):
        print(f'Grade {g}: {sum(subs.values())} questions -> {subs}')

if __name__ == '__main__':
    compile_all()
