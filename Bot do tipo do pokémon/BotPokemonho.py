import discord
from discord.ext import commands
from model import get_class
import os
import random
import requests 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            class_name, confidence = get_class("./keras_models.h5", "./labels.txt", f"./{attachment.filename}")
            await ctx.send(f"Classe: {class_name}, Confiança: {confidence:.2f}" )
    else:
        await ctx.send("Você esqueceu de enviar a imagem :(")

bot.run("")