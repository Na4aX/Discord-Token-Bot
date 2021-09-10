#!/usr/bin/python3.7

from bs4 import BeautifulSoup

import discord
import subprocess
import requests

def infos_wallets():
    add = {
            "wallet 1" : "https://bscscan.com/token/0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c?a=0x303966a54020e4ac44479bfa91b57fd826883d70",
            "wallet 2" : "https://bscscan.com/token/0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c?a=0x58677662e24593d6c7c6dab444da46f2a6a71833",
            "wallet dead" : "https://bscscan.com/token/0x40B165Fd5dDc75ad0bDDc9ADd0adAbff5431a975?a=0x000000000000000000000000000000000000dead"
    }

    for elm in add:
        cmc = requests.get(add[elm])
        soup = BeautifulSoup(cmc.content, 'html.parser')
        value = list(soup.find("div", {"id":"ContentPlaceHolder1_divFilteredHolderValue"}))[4][1:-2]
        balance = list(soup.find("div", {"id":"ContentPlaceHolder1_divFilteredHolderBalance"}))[2][1:-2] 

        value   = value.replace(",","")
        balance = balance.replace(",","")
        extension = balance.split()[1]
        reformat_balance = balance.split()[0].split(".")
        balance = reformat_balance[0] + "." + reformat_balance[1][:2] + " " + extension

        yield elm, value, balance



def info_coinsmarketcap():
    cmc = requests.get("https://coinmarketcap.com/currencies/memes-token/markets/")
    soup = BeautifulSoup(cmc.content, 'html.parser')

    data = soup.find('script', id="__NEXT_DATA__", type="application/json")

    coins = {}
    coins_data = json.loads(data.contents[0])
    listings = coins_data['props']['initialProps']['pageProps']['info']['statistics']
    return listings



async def info(message):

    volume = subprocess.check_output(["sh", "./curl_volume.sh"]).decode("utf-8")
    nb_holders = subprocess.check_output(["sh", "./curl_holders.sh"]).decode("utf-8")

    coinmarketcap_listings = info_coinsmarketcap()
    coinmarketcap_listings["volume"] = volume
    coinmarketcap_listings["Number of holders"] = nb_holders
    coinmarketcap_listings = {k: v for k, v in coinmarketcap_listings.items() if v}
    for i in coinmarketcap_listings:
        if coinmarketcap_listings[i]:
            if "Percentage" in i: 
                coinmarketcap_listings[i] = "{:.2f} %".format(coinmarketcap_listings[i])

    embed = discord.Embed(
                title       = "MEMES",
                color       = 0xff8000,
                url         = "https://bscscan.com/token/0x40b165fd5ddc75ad0bddc9add0adabff5431a975",
                description = "Contract : [0x40b165fd5ddc75ad0bddc9add0adabff5431a975](https://pancakeswap.finance/swap#/swap?outputCurrency=0x40b165fd5ddc75ad0bddc9add0adabff5431a975)"
            )

    choosen = {
        "price"                     : ":dollar: price",
        "priceChangePercentage1h"   : ":hourglass_flowing_sand: Price Change 1h",
        "priceChangePercentage24h"  : ":hourglass: Price Change 24h",
        "fullyDilutedMarketCap"     : ":classical_building: Market Cap",
        "rank"                      : ":trophy: rank",
        "highAllTime"               : ":arrow_up: ATH",
        "volumeYesterday"           : ":bar_chart: Volume yesterday",
        "Number of holders"         : ":family: Wallets"
        }

    for elm in choosen:
        embed.add_field(name=choosen[elm], value=str(coinmarketcap_listings[elm]), inline=True)

    wallets = { k : (v, b) for k, v, b in infos_wallets() }

    embed.add_field(name=":fire: burned", value=str(wallets["wallet dead"][1]), inline=True)

    value1=str(wallets["wallet 1"][0] + " / " + wallets["wallet 1"][1])
    value2=str(wallets["wallet 2"][0] + " / " + wallets["wallet 2"][1])
    embed.add_field(name=":coin: Wallet 1", value=value1, inline=True)
    embed.add_field(name=":coin: Wallet 2", value=value2, inline=True)

    await message.channel.send(embed=embed)

