'''
Faça um Programa que leia três números e mostre-os em ordem decrescente. (agora utilizando o laço de repetição)
'''

lista = []

for i in range(1,4):
  lista.append(input(f"Informe o {i}.o número: "))
  lista.sort(key=int, reverse=True)
print("A ordem decescente é:" ,lista)