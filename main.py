import discord
import os
import requests
import json
import random


client = discord.Client()

sad_words = ['triste', 'me siento solo', 'me siento sola', 'siento mal', 'deprimido', 'deprimida', 'cansada', 'cansado']  

iniciador_estimulos = ['Eres una persona valiosa.', 'Esto pasará, recuérdalo.', 'Siempre debes demostrarte a ti mismo lo valioso que eres.', 'Estoy a tu lado para apoyarte.']


#Frases motivadoras de API(english)
def get_quote():
  respuesta = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(respuesta.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#Inicio de Bot
@client.event
async def on_ready():
  print("Lest's do it: ".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('boom!motiv'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(iniciador_estimulos))  

client.run(os.getenv('DISCORD_TOKEN'))    



