import requests
import json


btc_url = 'https://api.coinlore.net/api/ticker/?id=90'
eth_url = 'https://api.coinlore.net/api/ticker/?id=80'

def get_btc_price():
    response = requests.get(url=btc_url)
    res = float(response.json()[0]['price_usd'])
    return f"{res:,}"

def get_eth_price():
    response = requests.get(url=eth_url)
    res = float(response.json()[0]['price_usd'])
    return f"{res:,}"

if __name__ == '__main__':
    get_btc_price()
    get_eth_price()