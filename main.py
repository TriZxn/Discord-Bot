import discord
import random
from keep_alive import keep_alive

client = discord.Client()

starter_buy = [
  "Definitely! :thumbsup: ",
  "buy, Buy, BUY!! :exclamation: ",
  "Eh, why not? :shrug:"
]

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

    if message.content.startswith('$hi'):
      await message.channel.send('Hello ' + message.author.name + '! :smile: ')
      print(message.author.name)
      print(message.author.id)
      print('Responded to their hello query')

    if message.content.startswith('$price'):
      await message.channel.send('https://www.binance.com/en/trade/DOGE_USDT?type=spot :money_with_wings: ')
      print(message.author.name)
      print(message.author.id) 
      print('Responded to their price query')

    if message.content.startswith('$shouldibuy'):
      await message.channel.send(random.choice(starter_buy))
      print(message.author.name)
      print(message.author.id)
      print('Responded to their buy query')

    if message.content.startswith('$TOTHEMOON'):
      await message.channel.send('BUCKLE UP, THE SPACESHIP IS 10 MINUTES FROM LIFTOFF!! :rocket: ')
      print(message.author.name)
      print(message.author.id)
      print('MOON GANG!')

    if message.content.startswith('$wallets'):
      await message.channel.send('https://multidoge.org/?dl=win and https://www.exodus.com/ work very well :thumbsup: ')
      print(message.author.name)
      print(message.author.id)
      print('Responded to the wallets query')

    if message.content.startswith('$help'):
      await message.channel.send('$helloshiba = Say hi to me! :smile: ')
      await message.channel.send('$pricedoge = Learn the price of dogecoin! :money_with_wings: ')
      await message.channel.send('$shouldibuy = Should you? :eyes: ')
      await message.channel.send('$TOTHEMOON = Help me encourage the investors! :rocket: ')
      await message.channel.send('$wallets = See what wallets are recommended! :thumbsup: ')
      print(message.author.name)
      print(message.author.id)
      print('Responded to their help query')

    if message.content.startswith('$commands'):
      await message.channel.send('$helloshiba = Say hi to me! :smile: ')
      await message.channel.send('$pricedoge = Learn the price of dogecoin! :money_with_wings: ')
      await message.channel.send('$shouldibuy = Should you? :eyes: ')
      await message.channel.send('$TOTHEMOON = Help me encourage the investors! :rocket: ')
      await message.channel.send('$wallets = See what wallets are recommended! :thumbsup: ')
      print(message.author.name)
      print(message.author.id)
      print('Responded to their help query')
    
    if message.content.startswith('$status'):
      await message.channel.send('https://Doge-Bot.bosszombie12345.repl.co')
      print(message.author.name)
      print(message.author.id)
      print('Responded to the status query')

keep_alive()
client.run('ODM5NzE3MTMxNDI3MjUwMTk2.YJNthQ.0UeYamqVWk7ZRfg1W8W53Uqdm2E')
