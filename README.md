# 🎵 Quiz Musical: Adivina la Canción

¡Bienvenido al Quiz Musical! Este es un juego web interactivo construido con Python y Flask donde pondrás a prueba tu conocimiento musical. Selecciona a tu artista favorito, escucha un pequeño fragmento de una canción real y demuestra que eres su mayor fan adivinando el título correcto.

---

## 🚀 Cómo funciona el juego

El proyecto está diseñado mediante una arquitectura Cliente-Servidor clásica, integrando herramientas de backend y frontend:

* **El Motor Web:** Desarrollado íntegramente en Python utilizando el micro-framework Flask.
* **El Proveedor de Datos:** Conectado en tiempo real a la API oficial de Deezer para obtener canciones, portadas y fragmentos de audio (previews) de forma completamente legal y gratuita.
* **El Flujo de Partida:** Al elegir un artista en la página principal, el servidor realiza una búsqueda dinámica, selecciona una canción al azar de entre su repertorio principal y envía el audio al navegador del jugador.
* **Memoria de Juego:** Se utilizan Sesiones encriptadas de Flask (`session`) para que el servidor recuerde de forma segura y oculta cuál es la canción que está sonando, impidiendo cualquier tipo de trampa por parte del usuario al inspeccionar el código.

---

## ⚖️ Reglas de Validación

Para garantizar una experiencia de juego justa y evitar frustraciones al teclear, el sistema de validación del código (gestionado en el archivo de funciones) aplica una limpieza exhaustiva a los textos antes de compararlos:

* **Insensibilidad a las mayúsculas y acentos:** El sistema convierte tanto la respuesta oficial de la base de datos como el intento del jugador a minúsculas. Escribir "Columbia" o "columbia" tiene el mismo resultado, así como "AHORA QUÉ" o "ahora que".
* **Caracteres no alfanuméricos:** Tampoco nos importan. Para el juego, "Hola!" y "Hola" es lo mismo.
* **Limpieza de espacios en blanco:** Se eliminan los espacios accidentales que el usuario pueda introducir al principio o al final de su respuesta.
* **Criterio de exactitud:** Una vez limpios ambos textos, la cadena de caracteres introducida debe coincidir con el título oficial de la canción que provee la API de Deezer.

---

## 🛠️ Guía de Instalación Local

Si quieres ejecutar este juego en tu propia máquina, elige uno de los siguientes dos métodos de instalación. Por motivos de ciberseguridad, este repositorio no incluye la clave de encriptación del servidor, por lo que deberás configurar tu propio entorno en el Paso 3.

### Opción A: Instalación Moderna (Recomendado - Requiere `uv`)

Este método utiliza el gestor de paquetes de alto rendimiento `uv`. Es el camino más rápido, seguro y compatible, ya que leerá el archivo `.python-version` y el `pyproject.toml` para aislar tu entorno en milisegundos.

**1. Clonar el repositorio y preparar la carpeta:**
Descarga los archivos del proyecto y abre tu terminal dentro de la carpeta principal.

**2. Sincronizar el entorno de forma automática:**
Ejecuta el siguiente comando en tu terminal:
`uv sync`

### Opción B: Instalación Tradicional (Sin uv - Requiere Python 3.13+)
Si prefieres usar el ecosistema nativo de Python, puedes construir el entorno a mano utilizando pip.

**1. Clonar el repositorio y preparar la carpeta:**
Descarga los archivos del proyecto y abre tu terminal dentro de la carpeta principal.

**2. Crear e instalar el entorno virtual manualmente:**
Ejecuta secuencialmente estos comandos en tu terminal según tu sistema operativo:

  a. En Windows:
  
  `python -m venv .venv`  
  `.venv\Scripts\activate`  
  `pip install flask requests python-dotenv`
  
  b. En macOS / Linux:
  
  `python3 -m venv .venv`  
  `source .venv/bin/activate`  
  `pip install flask requests python-dotenv`

### Pasos comunes a ambas opciones

**3. Configurar el Entorno Seguro (Variables de Entorno):**
Para que el sistema de sesiones funcione, necesitas proporcionar tu propia clave de seguridad local.
* Localiza el archivo llamado `.env.example` en la carpeta raíz.
* Haz una copia de ese archivo y renómbrala a `.env`.
* Abre tu nuevo archivo `.env` en cualquier editor de texto y cambia el valor por defecto por una contraseña inventada por ti (no uses espacios).
* *Nota:* El archivo `.env` es ignorado por Git de forma predeterminada para proteger tu sistema.

**4. Ejecutar el servidor:**
Con el entorno preparado y tu clave configurada, arranca el servidor web desde tu terminal:

  a. Si usaste la Opción A (uv):
  
  `uv run app.py`
  
  b. Si usaste la Opción B (Tradicional):
  (Asegúrate de tener el entorno virtual activado)
  
  `python app.py`

**5. ¡A jugar!**
Abre tu navegador web favorito (Chrome, Firefox, Safari) y escribe la siguiente dirección local en la barra de búsqueda para acceder a tu propia instancia del juego:
`http://127.0.0.1:5000`
