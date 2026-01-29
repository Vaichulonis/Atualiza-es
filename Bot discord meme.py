# Importações
import discord
import os
import random

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

# Mensagens aleatórias
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('++hello'):
        await message.channel.send("among us")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")

#---------------------------------------------------------
# parte que manda os memes com um comando
    elif message.content.startswith('$meme'):
        vari = r" Bote aqui o caminho para a sua pasta que está guardando os memes "
        img_name = random.choice(os.listdir(r' Bote aqui o caminho para a sua pasta que está guardando os memes '))
        with open(f'{vari}/{img_name}', "rb") as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

#------------------------------------------
# parte que manda outros memes com outro comando (opcional)
    elif message.content.startswith('$power'):
        vari = r" Bote aqui o caminho para a sua pasta que está guardando os memes "
        img_name = random.choice(os.listdir(r' Bote aqui o caminho para a sua pasta que está guardando os memes '))
        with open(f'{vari}/{img_name}', "rb") as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

#--------------------------------------
client.run("O seu toten")
