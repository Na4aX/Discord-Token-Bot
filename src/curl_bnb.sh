curl https://coinmarketcap.com/currencies/binance-coin/markets/ 2> /dev/null | grep -shoP '"priceValue ">\$.*?<' | grep -shoP '>\$.*?<'

# "priceValue ">$<
