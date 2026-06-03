# 🗺️ Hoja de Ruta del Proyecto (Roadmap)
El desarrollo de este proyecto se divide en cuatro fases principales, diseñadas para escalar la aplicación desde una lógica de consola básica hasta una plataforma web interactiva y conectada a servicios externos.

## Fase 1: Motor de validación y lógica base (Backend):
El objetivo de esta fase inicial es establecer el núcleo del juego en un entorno de consola utilizando Python, garantizando que la lógica de comprobación funcione de manera impecable antes de añadir capas de complejidad visual o sonora.

- Estructuras de datos: Implementación de las colecciones (diccionarios o listas) encargadas de almacenar y gestionar el catálogo de canciones y artistas disponibles para el juego.

- Algoritmo de limpieza y validación de texto: Dado que el jugador debe escribir el nombre exacto de la canción, se desarrollará un sistema de normalización de cadenas de texto (Strings). Este algoritmo se encarga de procesar la entrada del usuario (eliminando espacios redundantes, convirtiendo caracteres a minúsculas y suprimiendo tildes o caracteres especiales) para realizar una comparación precisa y flexible contra la base de datos de respuestas correctas.

## Fase 2: Integración de la API de Spotify
Esta fase transforma el proyecto de un entorno cerrado a una aplicación conectada al mundo real, utilizando la API oficial de Spotify para proveer el contenido multimedia.

- Gestión de credenciales y seguridad: Configuración de la aplicación en el portal Spotify for Developers y establecimiento de variables de entorno para manejar los tokens de acceso de forma segura, evitando su exposición en el repositorio público.

- Extracción de recursos de audio: Mediante la librería Spotipy, se implementarán scripts para consultar dinámicamente el repertorio del artista seleccionado. El sistema filtrará las respuestas de la API para extraer exclusivamente aquellas pistas que cuenten con un preview_url activo (un fragmento de audio de 30 segundos), descartando automáticamente las canciones que no dispongan de este recurso.

## Fase 3: Diseño de la interfaz web (Frontend estático)
Una vez asegurada la obtención de datos y la lógica de validación, el desarrollo se traslada a la creación de la capa visual de la aplicación web utilizando HTML5 y CSS3.

- Estructura del documento: Diseño del esqueleto visual enfocado en la usabilidad. Se reemplazará el clásico sistema de opciones por un formulario de entrada (<input type="text">) claro y accesible, diseñado para que el usuario introduzca el título de la canción.

- Diseño adaptable (Responsive Design): Aplicación de estilos para garantizar que el reproductor, el temporizador visual y el campo de entrada de texto mantengan una legibilidad y proporciones óptimas tanto en monitores de escritorio como en dispositivos móviles.

## Fase 4: Orquestación e interactividad (Flask + JavaScript)
La fase final consiste en la integración de los sistemas previos, creando un puente bidireccional entre el servidor (Python) y el cliente (Navegador) para ofrecer una experiencia en tiempo real.

- Despliegue del servidor con Flask: Implementación de un servidor backend ligero que se encargue de orquestar la aplicación, sirviendo las vistas HTML y transmitiendo de forma segura las URLs de los audios obtenidos de Spotify hacia la interfaz del usuario.

- Control de interactividad con JavaScript: Desarrollo del motor que rige la experiencia de juego en el navegador. Se programará el control del reproductor de audio, incluyendo un temporizador dinámico que interrumpa la reproducción exactamente al transcurrir el tiempo dictado por el nivel de dificultad (1, 3 o 5 segundos). Asimismo, JavaScript gestionará el envío asíncrono (sin recargar la página) de la respuesta del usuario hacia el servidor Flask para su posterior validación y suma de puntuación.
