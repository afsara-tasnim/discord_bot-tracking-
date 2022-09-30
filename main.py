import random
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
import chat
load_dotenv()



intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
#intents.message_content = True
allowed_mention = discord.AllowedMentions.all()

client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print("I am ready as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)
    msg = message.content
    # if any(word in msg.lower() for word in chat.links):
    #     await message.channel.send('Works')
    if msg.startswith("https://"):
        if msg in chat.links:
            await message.delete()
            await message.channel.send(message.author.mention)
            await message.channel.send(random.choice(chat.taunt))
        else:
            chat.links.append(msg)

    print(chat.links)


token = os.getenv('Token')
client.run(token)