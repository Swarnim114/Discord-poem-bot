import discord
import os
import random
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!poem'):
        try:
            response = requests.get("https://poetrydb.org/random")
            poem_data = response.json()[0]
            title = poem_data["title"]
            author = poem_data["author"]
            poem_lines = "\n".join(poem_data["lines"])
            poem = f"**{title}** by *{author}*\n\n{poem_lines}"
            await message.channel.send(poem)
        except Exception as e:
            await message.channel.send("Sorry, I couldn't fetch a poem right now.")

client.run(TOKEN)
