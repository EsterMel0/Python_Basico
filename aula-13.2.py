
import requests
import json

while True:

    req = requests.get('http://www.omdbapi.com/?apikey=5d9cabe3&s=' + input('Digite o nome do Filme: '))
    dict = json.loads(req.text)

    try:
        for t in dict['Search']:
            print("Título:", t['Title'])
            print("Ano:", t['Year'])
            print("")
        break

    except:
        print("Filme não encontrado\n")

        if req == 'SAIR':
            print("saindo..")
            break
        else:
            print("não entendi")

