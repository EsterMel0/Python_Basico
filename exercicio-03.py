'''
EXERCICIO 03: crie um programa que pergunte ao usuário a quantidade de convidados de uma festa, em seguida,
pergunte o nome dos convidados e imprima uma lista de convidados.
'''

quantidade = int(input("Informe a quantidade de pessoas convidadas: "))

nomes = []
for i in range(1, quantidade + 1):
  nomes.append(input(f"Nome do convidado numero {i} : "))


print("\n~~~~~~~~~~~~~~ Lista de Convidados ~~~~~~~~~~~~~~")
for i in nomes:
  print("-" ,i)
