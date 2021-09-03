#!/usr/bin/python3.7

async def usage(fct, message):
    ret = "Usage:\n\
    !price              - Display the current token price\n\
    !price <quantity>   - Convert number of token in dollar\n\
    !info               - Display Memestoken informations"
    if fct == "!price":
        ret = "usage:\n\
    !price               - Display the current token price\n\
    !price <quantity>    - Convert number of token in dollar"

    await message.channel.send(ret)

