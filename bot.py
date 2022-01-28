import discord
from configs import Token

client = discord.Client()

@client.event
async def on_ready():
    print (f'mulek ta vivo')

@client.event
async def on_message(msg):
    if msg.content.lower() == 'ola cumbot' or msg.content.lower() == 'ola cumboy' or msg.content.lower() == 'ola cumboy':
        await msg.channel.send('ola')

client.run(Token)