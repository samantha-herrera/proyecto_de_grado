import discord
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

NEWS_API_KEY = 'fd27fbfcedc2457f9a0a4c18a6190a14'

@bot.command()

async def noticias(ctx):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'cambio climático',
        'apiKey': NEWS_API_KEY, 
        'language': 'es', 
        'sortBy': 'publishedAt', 
        'pageSize': 3  
    }
    
    response = requests.get(url, params=params).json()
    
    if response['status'] == 'ok' and response['articles']:
        noticias = response['articles']
        for noticia in noticias:
            title = noticia['title']
            description = noticia['description']
            url = noticia['url']
            await ctx.send(f"**{title}**\n{description}\n[Leer más]({url})")
    
    else:
        await ctx.send("No se pudieron obtener noticias en este momento. Intenta más tarde.")

async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    
    if message.content.startswith('$hola'):
        await message.channel.send('¡Hola! Soy un ecobot, ¿En qué puedo colaborarte el día de hoy? (por favor antes de tu pregunta incluye un $, gracias)')
        
    elif message.content.startswith('$¿Qué es el cambio climático?'):
        await message.channel.send('El cambio climático no sólo es el aumento de las temperaturas medias, sino también las catástrofes naturales, los cambios en los hábitats de la fauna y la flora, la subida del nivel del mar y otros muchos efectos. Todos estos cambios se están produciendo a medida que el ser humano sigue añadiendo a la atmósfera gases de efecto invernadero que atrapan el calor, como el dióxido de carbono y el metano. Por orto lado, el calentamiento global son las consecuencias que generan la liberación de esos gases de efecto invernadero, pero este fenómeno en realidad está provocando diversos cambios en los patrones meteorológicos de la Tierra a largo plazo que varían según el lugar. Conforme la Tierra gira cada día, este nuevo calor gira a su vez, recogiendo la humedad de los océanos, aumentando y asentándose en diversos sitios, cambiando en definitiva el ritmo del clima al que todos los seres vivos nos hemos acostumbrado.')
        with open('images/imagen1.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
    
    elif message.content.startswith('$Dame un consejo'):
        await message.channel.send('Claro, aquí te presento un consejo que te puede ayudar, reduce el consumo de recursos, puedes usar las tres r (reducir, reciclar y reutilizar), puedes usar productos más sostenibles, como lo es el papel reciclado a la hora de hacer impresiones, e incluso puedes ahorrar agua, toma duchas mas cortas o cierra el grifo mientras te cepillas los dientes')
        with open('images/imagen5.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
    
    elif message.content.startswith('$Dame otro consejo'):
        await message.channel.send('Otro consejo que puedes implementar es reducir tu huella de carbono, esto mediante el uso de un transporte público o una bicicleta o ahorrando energia al apagar las luces, electrodomésticos y dispositivos que no estén en uso')
        with open('images/imagen4.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

    elif message.content.startswith('$Dame más imágenes sobre el tema'):
        await message.channel.send('Claro, aquí te dejo otras imágenes que te pueden interesar sobre este tema')
        with open('images/imagen3.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
        with open('images/imagen2.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

    elif message.content.startswith('$¿Qué otra cosa me recomiendas ver para informarme más acerca del tema?'):
        await message.channel.send('Si deseas informarte más sobre esto, te recomiendo ver diversos videos, entre ellos estos: https://youtu.be/LwRTw_7NNJs , https://youtu.be/NvNjz1dnwqQ , https://youtu.be/pLxKmRc3RoA . Estos provienen de páginas oficiales como la de la NASA o la de la ONU, espero te ayuden a resolver tus dudas')

    elif message.content.startswith('$Gracias'):
        await message.channel.send('No hay de que, me gusta haberte ayudado, estaré aquí si tienes más dudas con respecto al tema')
    
    else:
        await message.channel.send("No puedo entender tu pregunta, inentalo nuevamente")
    
    await bot.process_commands(message)

bot.run("MTMzMjEwMDEwMzM4MDUzNzUwNQ.GZfKnL.VRET8m8pzuHZk74WC0mVDzjciUIEAPOuvCoIpg")
