#!/usr/bin/python3.7
import subprocess

async def info(message):
    nb_holders = subprocess.check_output(["sh", "./curl_holders.sh"]).decode("utf-8")
    await message.channel.send("Number of holders : {}".format(nb_holders))
