# Story IP-USD Price Bot

Este es un bot para Discord que actualiza su apodo en todos los servidores en los que está presente con el precio actual de un token específico ($IP) en USD. El precio se obtiene cada 60 segundos a través de la API de CoinGecko y se actualiza en el apodo del bot con una flecha que indica si el precio ha subido o bajado.

## Características

- **Actualización de Apodo**: El bot actualiza su apodo cada 60 segundos con el precio actual de $IP en USD, mostrando una flecha que indica si el precio ha subido (`↗`) o bajado (`↘`).
- **Estado**: El bot tiene un estado estático que muestra "Watching Story IP-USD Price".
- **Compatibilidad**: El bot está diseñado para ser usado en múltiples servidores de Discord simultáneamente.

## Requisitos

Antes de usar el bot, asegúrate de tener lo siguiente:

- **Python 3.10 o superior**.
- **Poetry**: Para manejar las dependencias del proyecto.
- **Token de Discord**: El bot necesita un token de autenticación de Discord para funcionar.

## Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <nombre_del_directorio>
    ```

2. **Instalar las dependencias** con Poetry:
    ```bash
    poetry install
    ```

3. **Crear el archivo `.env`**:
   
   Copia el archivo `.env.example` a un archivo `.env` y agrega tu token de Discord:
   ```bash
   cp .env.example .env
   ```
   - Luego, abre el archivo .env y coloca tu token real de discord para el bot:
        DISCORD_TOKEN="tu_token_de_discord_aqui"

4. **Modificar variables del bot**:
    - Dentro de Bot.py puedes modificar a tu antojo los segundos que tarda en actualizarse el nombre del bot, el token de la api de coingecko, el estado del bot, etc.

5. **Ejecutar el bot**:
    ```bash
    poetry run python bot.py
    ```



Estructura de Archivos

   - bot.py: El archivo principal del bot.

   - .env.example: Ejemplo de archivo de configuración con el token de Discord.

   - pyproject.toml: Archivo de configuración de Poetry para gestionar las dependencias.

   - poetry.lock: Archivo de bloqueo de dependencias generado por Poetry.


Dependencias
Este proyecto usa las siguientes dependencias de Python:

  - discord.py: Una biblioteca de Python para interactuar con la API de Discord.

  - requests: Para hacer peticiones HTTP y obtener el precio de $IP.

  - python-dotenv: Para manejar las variables de entorno desde el archivo .env.

  - poetry: Para gestionar las dependencias y el entorno virtual.

Contribución
Si deseas contribuir a este proyecto, por favor realiza un fork y envía un pull request. Asegúrate de seguir las mejores prácticas y escribir código limpio.