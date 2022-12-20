import discord
import responses
import os
from discord.ext import tasks
from itertools import cycle



async def send_message(message, user_message, ans=False):
  response = responses.handle_response(user_message, message, ans)
  if ans:
    await message.reply(response, mention_author=False)
  else:    
    try:
      await message.channel.send(response)

    except Exception as e:
      print(e)


def run_bot():
  client = discord.Client(intents = discord.Intents.all())
  status = cycle(['Snake (Python)','The Game'])

  @client.event
  async def on_ready():
    print(f'{client.user} is running!')

    change_status.start()
    print(f'{client.user} is ready!')

  @tasks.loop(seconds=30)
  async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    user_message = str(message.content)

    o_ssi = client.get_user(int(os.getenv('o_ssi id')))

    if (o_ssi in message.mentions) or (client.user.mentioned_in(message)):
      await send_message(message, user_message, ans=True)
    else:
      await send_message(message, user_message)



  
  
  client.run(os.getenv('TOKEN'))



