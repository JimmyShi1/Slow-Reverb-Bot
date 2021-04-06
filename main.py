import discord

client = discord.Client()

@client.event
## Calls when login is sucessful, prints user info 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!r'):
    await message.channel.send('Test')

  client.run