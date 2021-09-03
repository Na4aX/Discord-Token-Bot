curl https://coinmarketcap.com/currencies/memes-token/ 2> /dev/null | grep -shoP 'trading volume of \$.*? USD' | cut -d " " -f 4 
