# ⚽ Fútbol Quiz: La Copa del Saber

Aplicación web educativa interactiva inspirada en la dinámica de partidos de fútbol y en las **Pruebas Saber del ICFES**. Combina preguntas académicas por grados y asignaturas con una mecánica de avance de balón, recuperación, retrocesos defensivos, disparos y goles.

---

## 🚀 Cómo Ejecutar la Aplicación

1. **Instalar dependencias** (si aún no se han instalado):
   ```bash
   npm install
   ```

2. **Iniciar el servidor web**:
   ```bash
   npm start
   # o directamente:
   node server.js
   ```

3. **Abrir en el navegador**:
   Entra en tu navegador en:
   👉 **http://localhost:3000**

---

## 🎮 Flujo del Usuario y Reglas del Juego

1. **Pantalla de Bienvenida:** Botones de Jugar, Instrucciones (con diagrama de flujo oficial) y Créditos.
2. **Personalización:** Ingreso de nombre/apodo, elección de selección nacional (Colombia 🇨🇴, Argentina 🇦🇷, Francia 🇫🇷, Portugal 🇵🇹, Alemania 🇩🇪), selección de jugador estrella y número de camiseta.
3. **Selección de Grado:** 6.º, 7.º, 8.º, 9.º, 10.º y 11.º (preparación Saber 11°).
4. **Modalidad de Preguntas:**
   - **Preguntas al Azar:** Reto interdisciplinar con preguntas de todas las áreas.
   - **Elegir Asignatura:** Matemáticas, Lenguaje / Lectura Crítica, Ciencias Naturales, Ciencias Sociales o Inglés.
5. **Modo de Juego:**
   - **Modo Solo:** Competición individual contra la Inteligencia Artificial del equipo rival con análisis pedagógico.
   - **Multijugador en Línea:** Creación de sala con código de 6 caracteres y código QR interactivo para escanear y competir en tiempo real mediante WebSockets.
6. **Mecánica del Partido en Cancha (Reglamentaria):**
   - La cancha cuenta con posiciones tácticas entre arco propio y arco rival.
   - **Respuesta Correcta:** Pase acertado y avance de 1 posición hacia la portería rival.
   - **Llegada al Arco:** ¡GOL! Sonido de celebración de gol, confeti, actualización de marcador (+1 gol) y reinicio al centro del campo.
   - **Respuesta Incorrecta:** Intercepción y pase de posesión/turno al rival.
   - **Regla de Recuperación:** Si el rival también se equivoca, el equipo original recupera la posesión del balón.
   - **Retroceso:** Si el recuperador vuelve a fallar consecutivamente, el balón retrocede una posición hacia su propio arco por seguridad defensiva.
   - **Puntos Académicos:** Marcador independiente de puntos (+100 por acierto) y efectividad %.
7. **Resultados Finales:** Entrega de la Copa del Saber, desglose de aciertos, efectividad y temas a reforzar para pruebas académicas.

---

## 📁 Estructura del Proyecto

```text
├── data/
│   ├── questions.json     # Base de datos estructurada de preguntas por grado, tema y dificultad (ICFES)
│   └── teams.json         # Catálogo de selecciones, jugadores, dorsales y colores
├── public/
│   ├── assets/
│   │   ├── banner.jpg     # Arte oficial de portada y jugadores
│   │   └── flowchart.png  # Diagrama de flujo de arquitectura
│   ├── css/
│   │   └── style.css      # Estilos deportivos modernos, cancha interactiva y glassmorphism
│   ├── js/
│   │   ├── audio.js       # Motor de audio sintetizado con Web Audio API (silbato, pases, ovación)
│   │   ├── qrcode.js      # Generador de códigos QR para salas multijugador
│   │   └── game.js        # Lógica del cliente, sincronización Socket.IO y simulación IA
│   └── index.html         # Vistas completas del juego y modales
├── server.js              # Servidor Express + Socket.IO en tiempo real y API REST
└── package.json           # Configuración del proyecto y dependencias
```

---

## 📝 Cómo Agregar Más Preguntas del ICFES

Puedes incorporar más preguntas directamente en [data/questions.json](file:///c:/Users/ESTUDIANTE/OneDrive/Documentos/Video%20Juego/data/questions.json) siguiendo esta estructura:

```json
{
  "id": "MAT-11-003",
  "grado": "11",
  "asignatura": "Matemáticas",
  "tema": "Trigonometría y funciones",
  "pregunta": "¿Cuál es el valor del ángulo en radianes equivalente a 180°?",
  "opciones": ["π / 2", "π", "2π", "3π / 2"],
  "correcta": 1,
  "explicacion": "Por definición de medida angular, 180° sexagesimales equivalen exactamente a π radianes.",
  "dificultad": "Fácil",
  "fuente": "Prueba Saber ICFES 11°"
}
```

---

## 👩‍🏫 Créditos y Dirección del Proyecto

- **Creadora y Directora General:** **Adrianys María Saumeth Padilla**
- **Áreas:** Diseño Pedagógico, Conceptualización y Gamificación Educativa de las Pruebas Saber ICFES.

---

## 🐙 Cómo Subir este Proyecto a GitHub

1. Inicializa el repositorio local en esta carpeta:
   ```bash
   git init
   ```
2. Agrega todos los archivos limpios (el archivo `.gitignore` ya se encargará de ignorar `node_modules` y archivos pesados):
   ```bash
   git add .
   ```
3. Realiza el primer commit:
   ```bash
   git commit -m "Versión final - Fútbol Quiz: La Copa del Saber"
   ```
4. Conecta con tu repositorio en GitHub y sube los cambios:
   ```bash
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/futbol-quiz-copa-del-saber.git
   git push -u origin main
   ```

---

## 🌐 Opciones de Despliegue en la Nube

Cuando decidas montarlo en internet, puedes publicarlo en cualquiera de estas opciones gratuitas con soporte de WebSockets:
- **Render.com** (Web Service Node.js gratuito con soporte de WebSockets)
- **Railway.app**
- **Vercel** o **Fly.io**
