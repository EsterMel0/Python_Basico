# API POKEMÓN

import requests
import json

try:
    req = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=10")



    pkmn = json.loads(req.text)

    for i in pkmn['results']:
        print(i)

except Exception as erro:
    print("ERRO:",erro)