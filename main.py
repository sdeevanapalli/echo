import discord
from discord import app_commands
from discord.ext import commands, tasks
import os
import datetime
from dotenv import load_dotenv
from random import choice
import json
import time
import requests
from pytz import timezone

load_dotenv()

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())

status = ['you!', 'messages!', '@everyone', 'for e.']


@client.event
async def on_ready():
    change_status.start()
    print("I'm online")
    print(client.user)
    await client.tree.sync()

@tasks.loop()
async def change_status(seconds=300):
    await client.change_presence(status=discord.Status.online,
                              activity=discord.Activity(
                                  type=discord.ActivityType.watching,
                                  name=(choice(status))))


token = os.environ.get('TOKEN')
client.run(token)
