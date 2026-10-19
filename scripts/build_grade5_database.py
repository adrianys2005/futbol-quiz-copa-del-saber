import re
import json
import os

def load_part1():
    with open('Cuadernillos de preguntas/saber5_parte1_extracted.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # Verified answer keys for Part 1:
    # Math: 50 questions
    math_answers = {
        1: 'B', 2: 'C', 3: 'B', 4: 'B', 5: 'B', 6: 'B', 7: 'B', 8: 'B', 9: 'B', 10: 'B',
        11: 'C', 12: 'B', 13: 'A', 14: 'B', 15: 'C', 16: 'C', 17: 'B', 18: 'B', 19: 'B', 20: 'C',
        21: 'B', 22: 'B', 23: 'B', 24: 'C', 25: 'B', 26: 'B', 27: 'B', 28: 'B', 29: 'B', 30: 'A',
        31: 'B', 32: 'A', 33: 'B', 34: 'B', 35: 'B', 36: 'B', 37: 'C', 38: 'B', 39: 'B', 40: 'A',
        41: 'B', 42: 'B', 43: 'B', 44: 'C', 45: 'B', 46: 'B', 47: 'B', 48: 'B', 49: 'A', 50: 'B'
    }

    # Sociales: 50 questions (numbered 51 to 100 in booklet)
    social_answers = {
        51: 'B', 52: 'B', 53: 'B', 54: 'B', 55: 'A', 56: 'B', 57: 'B', 58: 'B', 59: 'B', 60: 'B',
        61: 'A', 62: 'C', 63: 'B', 64: 'C', 65: 'B', 66: 'A', 67: 'B', 68: 'B', 69: 'A', 70: 'B',
        71: 'A', 72: 'A', 73: 'A', 74: 'B', 75: 'B', 76: 'A', 77: 'B', 78: 'A', 79: 'B', 80: 'A',
        81: 'B', 82: 'B', 83: 'A', 84: 'A', 85: 'A', 86: 'A', 87: 'A', 88: 'C', 89: 'A', 90: 'B',
        91: 'A', 92: 'B', 93: 'B', 94: 'B', 95: 'A', 96: 'A', 97: 'A', 98: 'B', 99: 'A', 100: 'A'
    }

    math_block = text.split('ASIGNATURA: MATEMÁTICAS')[1].split('ASIGNATURA: CIENCIAS SOCIALES')[0]
    social_block = text.split('ASIGNATURA: CIENCIAS SOCIALES')[1]

    letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

    pattern = r'Pregunta\s+(\d+)\s*\(([^)]+)\)\s*\n(.*?)\n([A-D]\..*?)(?=\nPregunta|\n===|\Z)'

    questions = []

    # Parse Math
    for num_s, tema, prompt, opt_block in re.findall(pattern, math_block, re.DOTALL):
        num = int(num_s)
        opts = []
        for line in opt_block.strip().split('\n'):
            line_clean = line.strip()
            if re.match(r'^[A-D]\.\s*', line_clean):
                opts.append(re.sub(r'^[A-D]\.\s*', '', line_clean))
        
        corr_letter = math_answers.get(num, 'A')
        corr_idx = letter_to_idx[corr_letter]

        diff = "Fácil" if num in [1, 3, 5, 6, 8, 14, 18, 29, 31, 33, 39, 45, 49, 50] else ("Difícil" if num in [10, 11, 20, 22, 24, 25, 27, 35, 43, 44] else "Medio")

        questions.append({
            "id": f"MAT-05-{num:02d}",
            "grado": "5",
            "asignatura": "Matemáticas",
            "tema": tema.strip(),
            "pregunta": prompt.strip(),
            "opciones": opts,
            "correcta": corr_idx,
            "explicacion": f"La opción correcta es la ({corr_letter}): {opts[corr_idx]}.",
            "dificultad": diff,
            "fuente": "Cuadernillo ICFES Saber 5° Oficial - Matemáticas",
            "tiempoLimite": 120 if diff == "Difícil" else (90 if diff == "Fácil" else 105)
        })

    # Parse Sociales
    for num_s, tema, prompt, opt_block in re.findall(pattern, social_block, re.DOTALL):
        num = int(num_s)
        opts = []
        for line in opt_block.strip().split('\n'):
            line_clean = line.strip()
            if re.match(r'^[A-D]\.\s*', line_clean):
                opts.append(re.sub(r'^[A-D]\.\s*', '', line_clean))
        
        corr_letter = social_answers.get(num, 'A')
        corr_idx = letter_to_idx[corr_letter]

        diff = "Fácil" if num in [53, 54, 55, 62, 65, 66, 79, 81, 83, 90, 92, 99] else ("Difícil" if num in [51, 63, 71, 74, 84, 87, 88, 94, 97] else "Medio")

        questions.append({
            "id": f"SOC-05-{(num-50):02d}",
            "grado": "5",
            "asignatura": "Ciencias Sociales",
            "tema": tema.strip(),
            "pregunta": prompt.strip(),
            "opciones": opts,
            "correcta": corr_idx,
            "explicacion": f"La opción correcta es la ({corr_letter}): {opts[corr_idx]}.",
            "dificultad": diff,
            "fuente": "Cuadernillo ICFES Saber 5° Oficial - Sociales y Ciudadanas",
            "tiempoLimite": 110 if diff == "Difícil" else (90 if diff == "Fácil" else 100)
        })

    return questions

def load_part2():
    with open('Cuadernillos de preguntas/banco_completo_icfes_saber_5_parte_2.md', 'r', encoding='utf-8') as f:
        text = f.read()

    letter_to_idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

    # Extract answer keys
    keys_section = text.split('## CLAVE DE RESPUESTAS')[1]
    
    # Naturales answers
    cn_key_text = re.search(r'CIENCIAS NATURALES\*\*(.*?)(?=###|\Z)', keys_section, re.DOTALL | re.IGNORECASE).group(1)
    cn_keys = {int(num): ltr for num, ltr in re.findall(r'(\d+)\.\s*([A-D])', cn_key_text)}

    # Inglés answers
    ing_key_text = re.search(r'INGL[EÉ]S\*\*(.*?)(?=###|\Z)', keys_section, re.DOTALL | re.IGNORECASE).group(1)
    ing_keys = {int(num): ltr for num, ltr in re.findall(r'(\d+)\.\s*([A-D])', ing_key_text)}

    # Lectura Crítica answers
    lc_key_text = re.search(r'LECTURA CR[IÍ]TICA\*\*(.*?)(?=###|\Z)', keys_section, re.DOTALL | re.IGNORECASE).group(1)
    lc_keys = {int(num): ltr for num, ltr in re.findall(r'(\d+)\.\s*([A-D])', lc_key_text)}

    mod3_text = text.split('## MÓDULO 3: CIENCIAS NATURALES')[1].split('## MÓDULO 4: INGLÉS')[0]
    mod4_text = text.split('## MÓDULO 4: INGLÉS')[1].split('## MÓDULO 5: LECTURA CRÍTICA')[0]
    mod5_text = text.split('## MÓDULO 5: LECTURA CRÍTICA')[1].split('## CLAVE DE RESPUESTAS')[0]

    questions = []

    # 1. Ciencias Naturales (50)
    # Sections inside CN: Entorno Vivo (1-20), Entorno Físico (21-38), CTS (39-50)
    cn_pattern = r'\*\*(\d+)\.\s*(.*?)(?=\n\*\*\d+\.|\Z)'
    for num_s, block in re.findall(cn_pattern, mod3_text, re.DOTALL):
        num = int(num_s)
        lines = block.strip().split('\n')
        prompt_lines = []
        opts = []
        for line in lines:
            line_s = line.strip()
            if re.match(r'^[A-D][\)\.]\s+', line_s):
                opts.append(re.sub(r'^[A-D][\)\.]\s+', '', line_s))
            elif not opts:
                prompt_lines.append(line_s)
        
        prompt = ' '.join(prompt_lines).strip()
        prompt = prompt.replace('**', '')

        tema = "Entorno Vivo" if num <= 20 else ("Entorno Físico" if num <= 38 else "Ciencia, Tecnología y Sociedad")
        diff = "Fácil" if num in [1, 4, 5, 9, 14, 21, 23, 30, 39, 45] else ("Difícil" if num in [6, 11, 13, 20, 26, 33, 36, 42, 49] else "Medio")
        corr_letter = cn_keys.get(num, 'A')
        corr_idx = letter_to_idx[corr_letter]

        questions.append({
            "id": f"NAT-05-{num:02d}",
            "grado": "5",
            "asignatura": "Ciencias Naturales",
            "tema": tema,
            "pregunta": prompt,
            "opciones": opts,
            "correcta": corr_idx,
            "explicacion": f"La opción correcta es la ({corr_letter}): {opts[corr_idx]}.",
            "dificultad": diff,
            "fuente": "Cuadernillo ICFES Saber 5° Oficial - Ciencias Naturales",
            "tiempoLimite": 110 if diff == "Difícil" else (90 if diff == "Fácil" else 100)
        })

    # 2. Inglés (50)
    # Texts for Inglés
    text1_farm = """[Reading: "A Day at the Farm"]
Hello, my name is Lucas. Every Saturday, I visit my grandparents' farm. They have three cows, two horses, and many chickens. In the morning, I help my grandfather collect eggs from the coop. My grandmother makes fresh cheese with the milk from the cows. I love riding the brown horse across the green fields. It is my favorite place in the world!"""

    text2_school = """[Reading: "The Green School Project"]
Our school started an eco-friendly project last month. Students organized three teams: recycling plastic bottles, planting flowers in the garden, and turning off the lights in empty classrooms. My teacher, Ms. Ramirez, says that small actions make a big difference for our planet. We won a prize for the cleanest school in the city!"""

    ing_pattern = r'\*\*(\d+)\.\s*(.*?)(?=\n\*\*\d+\.|\Z)'
    for num_s, block in re.findall(ing_pattern, mod4_text, re.DOTALL):
        num = int(num_s)
        lines = block.strip().split('\n')
        prompt_lines = []
        opts = []
        for line in lines:
            line_s = line.strip()
            if re.match(r'^[A-D][\)\.]\s+', line_s):
                opts.append(re.sub(r'^[A-D][\)\.]\s+', '', line_s))
            elif not opts:
                prompt_lines.append(line_s)
        
        prompt = ' '.join(prompt_lines).strip().replace('**', '')

        # Attach reading text context for questions 39-50
        if 39 <= num <= 44:
            prompt = f"{text1_farm}\n\n{prompt}"
        elif 45 <= num <= 50:
            prompt = f"{text2_school}\n\n{prompt}"

        tema = "Vocabulario" if num <= 10 else ("Diálogos" if num <= 25 else ("Gramática" if num <= 38 else "Comprensión de Lectura"))
        diff = "Fácil" if num in [1, 2, 7, 11, 12, 13, 26, 29, 32, 38] else ("Difícil" if num in [10, 24, 27, 35, 37, 43, 48, 50] else "Medio")
        corr_letter = ing_keys.get(num, 'A')
        corr_idx = letter_to_idx[corr_letter]

        questions.append({
            "id": f"ING-05-{num:02d}",
            "grado": "5",
            "asignatura": "Inglés",
            "tema": tema,
            "pregunta": prompt,
            "opciones": opts,
            "correcta": corr_idx,
            "explicacion": f"The correct answer is ({corr_letter}): {opts[corr_idx]}.",
            "dificultad": diff,
            "fuente": "Cuadernillo ICFES Saber 5° Oficial - Inglés",
            "tiempoLimite": 120 if (39 <= num <= 50 or diff == "Difícil") else 95
        })

    # 3. Lectura Crítica (50)
    # Texts in Lectura Crítica:
    texts_lc = {
        (1, 4): """[Texto: "El secreto de las hormigas cortadoras de hojas"]
Las hormigas cortadoras de hojas son famosas por transportar trozos de hojas a través del bosque. En realidad, no pueden digerir la celulosa dura de las hojas. Ellas utilizan los fragmentos vegetales como abono para cultivar un hongo especial dentro de sus galerías subterráneas. Este hongo es su verdadero y único alimento. Si el hongo muere, la colonia entera corre el riesgo de desaparecer.""",
        (5, 8): """[Texto: "La fabulosa fábula del león y el ratón"]
Un fiero león dormía en la selva cuando un pequeño ratón correteó sobre su nariz. El león despertó enojado y atrapó al ratón entre sus garras. El ratoncito suplicó: "—¡Rey de la selva, perdóneme! Si me deja vivir, algún día podré ayudarlo". El león soltó una carcajada y lo dejó libre. Días después, el león cayó en una red de cazadores. Al escucharlo rugir, el ratón llegó y comenzó a roer las cuerdas hasta liberarlo.""",
        (9, 12): """[Texto: "Infografía sobre el cuidado del agua"]
El 97% del agua del planeta es salada y solo el 3% es agua dulce apta para el consumo humano. La mayor parte está congelada en glaciares. Acciones clave: cerrar la llave al cepillarse (ahorra 10 litros), duchas de 5 minutos (ahorra 50 litros) y reparar goteras.""",
        (13, 16): """[Texto: "La bicicleta: el transporte del futuro"]
La bicicleta no contamina el aire, reduce el tráfico vehicular y mejora la salud cardiovascular del ciclista. Es uno de los inventos más eficientes y ecológicos de la historia.""",
        (17, 20): """[Texto: Poema "El Rastrojo"]
El viento silba entre las ramas secas,
la tierra sueña con la lluvia fresca.
En el rastrojo duerme la semilla,
esperando el agua que despierte su orilla.""",
        (21, 24): """[Texto: "El descubrimiento del fuego"]
El control del fuego por los primeros humanos permitió cocinar alimentos, ahuyentar a los depredadores nocturnos, protegerse del frío y extender las horas de actividad comunitaria.""",
        (25, 27): """[Texto: Diálogo sobre las redes sociales]
Camila: —Pienso que las redes sociales son fantásticas para mantenernos comunicados con familiares lejanos si se usan con moderación.
Mateo: —Yo creo que a veces nos quitan demasiado tiempo y distancian las conversaciones cara a cara."""
    }

    lc_pattern = r'\*\*(\d+)\.\s*(.*?)(?=\n\*\*\d+\.|\Z)'
    for num_s, block in re.findall(lc_pattern, mod5_text, re.DOTALL):
        num = int(num_s)
        lines = block.strip().split('\n')
        prompt_lines = []
        opts = []
        for line in lines:
            line_s = line.strip()
            if re.match(r'^[A-D][\)\.]\s+', line_s):
                opts.append(re.sub(r'^[A-D][\)\.]\s+', '', line_s))
            elif not opts:
                prompt_lines.append(line_s)
        
        prompt = ' '.join(prompt_lines).strip().replace('**', '')

        # Check if text context belongs to this question
        for (r_start, r_end), passage in texts_lc.items():
            if r_start <= num <= r_end:
                prompt = f"{passage}\n\n{prompt}"
                break

        tema = "Comprensión Textual" if num <= 16 else ("Poesía y Narrativa" if num <= 27 else "Lógica y Argumentación")
        diff = "Fácil" if num in [1, 5, 9, 13, 18, 28, 30, 34, 41, 49] else ("Difícil" if num in [4, 8, 11, 20, 27, 33, 38, 43, 50] else "Medio")
        corr_letter = lc_keys.get(num, 'A')
        corr_idx = letter_to_idx[corr_letter]

        questions.append({
            "id": f"LEC-05-{num:02d}",
            "grado": "5",
            "asignatura": "Lectura Crítica",
            "tema": tema,
            "pregunta": prompt,
            "opciones": opts,
            "correcta": corr_idx,
            "explicacion": f"La opción correcta es la ({corr_letter}): {opts[corr_idx]}.",
            "dificultad": diff,
            "fuente": "Cuadernillo ICFES Saber 5° Oficial - Lectura Crítica",
            "tiempoLimite": 120 if (num <= 27 or diff == "Difícil") else 100
        })

    return questions

def main():
    q_part1 = load_part1()
    print(f"Loaded {len(q_part1)} questions from Part 1 (Math & Social)")
    
    q_part2 = load_part2()
    print(f"Loaded {len(q_part2)} questions from Part 2 (Naturales, Inglés, Lectura)")

    all_grade5 = q_part1 + q_part2
    print(f"Total Grade 5 questions: {len(all_grade5)}")

    # Load existing questions.json
    questions_file = 'public/data/questions.json'
    with open(questions_file, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)

    print(f"Existing questions before adding: {len(existing_data)}")
    
    # Remove any existing grade 5 if any
    filtered = [q for q in existing_data if str(q.get('grado')) != '5']

    # Prepend or append Grade 5 questions
    final_questions = all_grade5 + filtered

    print(f"Total questions after merging: {len(final_questions)}")

    with open(questions_file, 'w', encoding='utf-8') as f:
        json.dump(final_questions, f, ensure_ascii=False, indent=2)

    print(f"Successfully saved {len(final_questions)} questions to {questions_file}!")

if __name__ == '__main__':
    main()
