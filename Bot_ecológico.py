#Importações
import discord

comandos = {"$help", "$what", "$cause", "$problems", "$do"}

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

  #Comandos
    if message.content.startswith('$help'):
        await message.channel.send("Esses são os comandos disponíveis no momento:", comandos)
    
    elif message.content.startswith("$what"):
        await message.channel.send("A poluição é a introdução de coisas que degradam o meio ambiente e prejudicam a saúde humana.")

    elif message.content.startswith("$cause"):
        await message.channel.send("A poluição pode causar problemas respiratórios, alergias, dores de cabeça e fadiga.")
    
    elif message.content.startswith("$problems"):
        await message.channel.send("Dentre os principais problemas estão: produtos de limpeza químicos, mofo, poeira, fumaça e lixos.")

    elif message.content.startswith("$do"):
        await message.channel.send("Alguns dos cuidados que você pode ters são: jogar o lixo no lixo, lavar a louça após as refeições, tirar as fezes dos seus animais (se tiver), limpar a casa.")

client.run("Bote o seu totem aqui")
