import datetime
import time
import requests
import json

req = None

while True:
    try:
        req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL')
        dict = json.loads(req.text)

        print("--- COTAÇÃO ---", datetime.datetime.now())
        print("Dólar:", dict["USDBRL"]['high'])
        print("Euro:", dict["EURBRL"]['high'])
        time.sleep(5)
        print("")

    except:
        print("erro na conexão")
        exit()


