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
      await message.channel.send('Hello ' + message.author.name + '! :smile: ')
      print(message.author.name)
      print(message.author.id)
      print('Responded to their hello query')

keep_alive()
client.run('ODM5NzE3MTMxNDI3MjUwMTk2.YJNthQ.0UeYamqVWk7ZRfg1W8W53Uqdm2E')
