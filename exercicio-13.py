'''
EXERCICIO: escreva uma função que receba um objeto de coleção (lista, etc.) e retorne o valor do maior número dentro dessa coleção,
sem seguida faça uma função que retorne o menor número da coleção
'''
quantidade = int(input("Quantos números deseja informar?\n >>"))

lista = []

for i in range(1, quantidade+1):
    lista.append(input(f"Informe o {i}° número: "))

print(lista)
print("O maior número da coleção é:", max(lista))
print("O menor número da coleção é:", min(lista))

