import re
import requests

string_de_teste = requests.get("https://loucosporcoxinha.com.br/")

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', string_de_teste.text) # .findall se utiliza para procurar por tudo

if padrao:
    print(padrao)
else:
    print("Padrao não encontrado.")