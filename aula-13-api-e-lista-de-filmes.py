# API: são 'interfaces' utilizadas para se comunicar com outros programas que pode ser usado para fazer requisições

import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=5d9cabe3&s='+ titulo + '&type=movie')
        dicionario = json.loads(req.text)  # o '.loads' pega um texto estruturado em json e o transforma em um dicionário
        return dicionario
    except:
        print("erro na conexão")
        return None


def printar_detalhes(filme):
    print('Título:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Atores:', filme['Actors'])
    print("")


sair = False
while not sair:
    op = input("Escreva o nome de um filme ou SAIR para fechar: ")

    if op == 'SAIR':
        sair = True
        print("Saindo...")
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print("Filme não encontrado")
        else:
            printar_detalhes(filme)