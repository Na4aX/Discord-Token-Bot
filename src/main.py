#!/usr/bin/python3.7

import discord
import subprocess
import os

from price import price
from info import info
from usage import usage

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    message.content = message.content.lower()
    cmd = message.content.split()[0]
    state = 0
    if cmd == "!price":
        await price(message)
    elif message.content == "!info":
        await info(message)
    elif state == -1:
        await usage(cmd, message)


API_KEY = os.environ.get("DISCORD_API_KEY")
client.run(API_KEY)
