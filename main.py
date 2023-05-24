import asyncio
import discord
from discord.ext import commands
import discord_plays
import help
import json
import pyttsx3
import keyboard

intents = discord.Intents.all()
bot = commands.Bot('.', intents=intents)
tts = pyttsx3.init()
tts.setProperty("volume", 0.25)

starting_message = """  
*****

Let's play a game: write the commands in order to play. For a list of commands type "help".

*****
"""


async def countdown():
    startchannel = bot.get_channel(channel_id)
    await startchannel.send("starting in:")
    await startchannel.send("3")
    tts.say('3')
    tts.runAndWait()
    await asyncio.sleep(1)
    await startchannel.send("2")
    tts.say('2')
    tts.runAndWait()
    await asyncio.sleep(1)
    await startchannel.send("1")
    tts.say('1')
    tts.runAndWait()
    await asyncio.sleep(1)
    await startchannel.send("GOOOOO")
    tts.say('GOOOOO')
    tts.runAndWait()


@bot.event
async def on_ready():
    print("bot started")
    tts.say('bot started')
    tts.runAndWait()

    startchannel = bot.get_channel(channel_id)
    await startchannel.send(starting_message)
    await countdown()


@bot.event
async def on_message(message):
    command = str(message.content.lower())
    author = str(message.author)

    print(f'{author}: {command}')

    if command == "help":
        # modify the help function depending on the game
        await message.channel.send(help.mario())

    if command == "thx":
        # for good courtesy
        await message.channel.send("With pleasure")

    await discord_plays.play_mario(command)

    # you can add as many games as you'd like in the discord_plays file


if __name__ == '__main__':
    f = open('config.json')
    file = json.load(f)
    token = file["token"]
    channel_id = int(file["startchannelid"])
    f.close()
    bot.run(token)

