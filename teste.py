import requests
import json
import pprint # imprime 'bonitinho'


req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL')
dict = json.loads(req.text)

pprint.pprint(dict)