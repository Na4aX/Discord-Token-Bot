#!/usr/bin/python3.7
import subprocess

async def info(message):
    nb_holders = subprocess.check_output(["sh", "./curl_holders.sh"]).decode("utf-8")
    volume = subprocess.check_output(["sh", "./curl_volume.sh"]).decode("utf-8")
    await message.channel.send(
        f"Number of holders : {nb_holders}"
        f"Volume in 24h : {volume}")
