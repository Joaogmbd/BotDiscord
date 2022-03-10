#importando libs
import discord
from discord.ext import commands
import random as r
import datetime

#credenciais
TOKEN = '<token>'

client = commands.Bot(command_prefix='R!')

#Inicializando BOT
@client.event
async def on_ready():
    print('Conectado ao bot: {}'.format(client.user.name))
    print('Meu id é: {}'.format(client.user.id))

#Comandos
@client.command()
async def mensagem(msg):
    textos = ['eae','oi','ola','batata']
    await msg.send(textos[r.randint(0,3)])
    print('um comando foi enviado')

@client.command()
async def humor(msg):
    current_time = datetime.datetime.now()
    dia = int(current_time.day)
    if (dia %2 == 0):
        await msg.send('Hoje eu to BOLADO! \U0001F621')
    else:
        await msg.send('Hoje eu to FELIZINHO! \U0001f604')
    print('um comando foi enviado')

#rodando o bot
client.run(TOKEN)

