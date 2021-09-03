curl https://coinmarketcap.com/currencies/memes-token/markets/ 2> /dev/null | grep -E -o '>\$0\.[0-9]+<' | uniq | tail
