#!/usr/bin/python3.7

import subprocess
from usage import usage


def parse(nb, end):
    if end == "t":
        return float(nb) * 10**12
    elif end == "b":
        return float(nb) * 10**9
    elif end == "m":
        return float(nb) * 10**6
    return float(nb)


async def price(message):
    content = message.content.split()
    if content[0] != "!price":
        await usage("", message)

    clean = lambda x : x.replace(">$",'').replace("<","").replace("\n","")

    price_meme = subprocess.check_output(["sh", "./curl.sh"]).decode("utf-8") 
    price_meme = float(clean(price_meme))

    if len(content) == 1:
        await message.channel.send("${0:.4e}".format(price_meme))
    
    elif len(content) >= 2:
        try:
            nb = content[1]
            postfix = nb[-1].lower()

            if postfix in ["b","t","m"]:
                nb = nb[:-1]

            nb = parse(nb, postfix)

            price_bnb = subprocess.check_output(["sh", "./curl_bnb.sh"]).decode("utf-8") 
            price_bnb = float(clean(price_bnb))

            result = price_meme * nb / price_bnb * price_bnb
            result_bnb = price_meme * nb / price_bnb

            fmt = "\t${:.4f}" if result > 0.0001 else "\t${0:.4e}"

            await message.channel.send(fmt.format(result))
            await message.channel.send("\t{:.4f} BNB".format(result_bnb))

        except:
            await usage("!price", message)

