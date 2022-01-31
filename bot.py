import discord
from dotenv import load_dotenv
from os import getenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print('mulek ta vivo')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if msg.content.lower() in ('ola cumbot', 'ola cumboy'):
        await msg.channel.send(f'ola {msg.author.mention}')

client.run(getenv('TOKEN'))