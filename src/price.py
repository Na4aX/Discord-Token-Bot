#!/usr/bin/python3.7

import subprocess
from usage import usage

clean= lambda x : x.replace(">$",'').replace("<","").replace("\n","")

async def price(message):
    print(message.content)
    content = message.content.split()
    if content[0] != "!price":
        await usage("", message)


    length = len(content)

    price_meme = subprocess.check_output(["sh", "./curl.sh"]).decode("utf-8") 
    price_meme = float(clean(price_meme))

    if len(content) == 1:
        await message.channel.send("${0:.4e}".format(price_meme))
    
    elif length >= 2:
        try:
            nb = float(content[1].replace('\n',''))
            price_bnb = subprocess.check_output(["sh", "./curl_bnb.sh"]).decode("utf-8") 
            price_bnb = float(clean(price_bnb))
            result = price_meme * nb / price_bnb * price_bnb
        
            if result > 0.0001:
                await message.channel.send("${:.4f}".format(result*0.95))
            else:
                await message.channel.send("${0:.4e}".format(result*0.95))
        except:
            await usage("!price", message)
