import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')
      if message.author.id == 291609497057886209:
          print('Responded to TriZxn hello query')

    if message.content.startswith('$price'):
      await message.channel.send('*Price*')
      if message.author.id == 291609497057886209:
          print('Responded to TriZxn price query')
      
client.run('ODM5NzE3MTMxNDI3MjUwMTk2.YJNthQ.0UeYamqVWk7ZRfg1W8W53Uqdm2E')
