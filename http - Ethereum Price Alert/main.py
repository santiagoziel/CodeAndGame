from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, time
import requests

url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
#1027 Id for ethereum
parameters = {
  'amount':'1',
  'id':'1027',
  'convert':'USD'
}

  #para obtener una api key de coin coinmarketcap visita https://coinmarketcap.com/api/documentation/v1/
headers = {
  'Accepts': 'application/json',
  "Accept-Encoding": "deflate, gzip",
  'X-CMC_PRO_API_KEY': '<TU API KEY>',
}


session = Session()
session.headers.update(headers)

PreviusPrice = 0

url_monkey_trigger = "https://api.voicemonkey.io/trigger"

check_below = 3643
check_above = 3666
#para obtener un voice monkey acces y secret token visita https://voicemonkey.io/start
def call_monkey(monkey):
    payload = {
    "access_token":"<TU ACCESS TOKEN>",
    "secret_token":"<TU SECRET TOKEN>",
    "monkey":monkey
    }
    r = requests.post(url_monkey_trigger , json = payload)
def checkBit(PreviusPrice):
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        CurrentPrice = float(data["data"]['quote']["USD"]["price"])
        if CurrentPrice < check_below:
            call_monkey("<Nombre De tu trabajador de bajada>")
        elif (CurrentPrice > check_above):
            call_monkey("<Nombre De tu trabajador de Subida>")
        print(f"Current Price {CurrentPrice}, previus price {PreviusPrice}")
        return CurrentPrice
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return 1

while True:
    #logica para determinar si se necesit amandar alerta
    PreviusPrice = checkBit(PreviusPrice)
    if PreviusPrice > check_above or PreviusPrice < check_below:
        break
    time.sleep(60)
