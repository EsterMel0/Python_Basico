import re

string_de_teste = "o gato é bonito"

padrao = re.search(r'\w\w\w\w\w\w', string_de_teste) # r significa RAW STRING, que seria uma string crua

if padrao:
    print(padrao.group())
else:
    print("Padrão não encontrado")