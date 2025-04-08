import discord
from discord.ext import tasks
import requests
import asyncio
import os
import logging
from dotenv import load_dotenv

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Cargar variables de entorno desde .env (no olvides cambiar de nombre el .env.example o crear un .env nuevo)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    logger.error("No se encontró el token en el archivo .env. Asegúrate de configurarlo.")
    exit(1)

# Configurar intents
intents = discord.Intents.default()  # Intents básicos
intents.presences = True  # Habilita el intent de presence (nota la "s")
client = discord.Client(intents=intents)

# Variable para rastrear el precio anterior (para las flechas) empezando con 0
last_price = 0

# Función para obtener el precio del $IP
def get_ip_price():
    try:
        # Reemplaza con la API correcta para tu token puedes revisarlo en https://api.coingecko.com/api/v3/coins/list
        url = "https://api.coingecko.com/api/v3/simple/price?ids=story-2&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        logger.info(f"Data cruda de CoinGecko: {data}")
        # Verificar si la respuesta contiene el precio esperado
        price = data.get("story-2", {}).get("usd", 0)
        return price
    except Exception as e:
        logger.error(f"Error obteniendo precio: {e}")
        return 0

# Tarea para actualizar el apodo cada 60 segundos (ajustable)
@tasks.loop(seconds=60)
async def update_nickname():
    global last_price
    price = get_ip_price()
    # Comparar si los precios son iguales para evitar cambios innecesarios
    if last_price == price:
        logger.info("El precio no ha cambiado.")
        return    
    # Determinar la flecha según el cambio de precio
    arrow = "↗" if price > last_price else "↘" if price < last_price else ""
    last_price = price
    new_name = f"${price:.4f} ({arrow})"

    # Actualizar el apodo del bot en todos los servidores donde está presente
    for guild in client.guilds:
        try:
            await guild.me.edit(nick=new_name)
            logger.info(f"Apodo actualizado a: {new_name} en {guild.name}")
        except discord.errors.HTTPException as e:
            logger.warning(f"Error actualizando apodo en {guild.name}: {e} (posible rate limit)")

# Evento cuando el bot se conecta
@client.event
async def on_ready():
    logger.info(f"Bot conectado como {client.user}")
    # Establecer un estado estático
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Story IP-USD Price"))
    if not update_nickname.is_running():
        update_nickname.start()  # Inicia la tarea del apodo


# Evento cuando el bot se une a un nuevo servidor
@client.event
async def on_guild_join(guild):
    global last_price
    logger.info(f"El bot se unió a un nuevo servidor: {guild.name}")
    price = get_ip_price()
    arrow = "↗" if price > last_price else "↘" if price < last_price else ""
    last_price = price
    new_name = f"${price:.4f} ({arrow})"

    try:
        await guild.me.edit(nick=new_name)
        logger.info(f"Apodo inicial establecido en: {new_name} en {guild.name}")
    except discord.errors.HTTPException as e:
        logger.warning(f"No se pudo establecer el apodo inicial en {guild.name}: {e}")

# Corre el bot
client.run(TOKEN)


