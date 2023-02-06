import os
'''
AULA 02: ENTRADA DE DADOS, SAIDA E TIPOS DE VARIAVEIS
'''

print("~~~~~~~~~Entrada de Dados~~~~~~~~")
nome = input("Informe seu nome: ")
idade = 19
altura = 1.52
tipo_nome = type(nome) #type vai printar na tela qual o tipo da variavel descrita entre parenteses
tipo_idade = type(idade)
tipo_altura = type(altura)

print("\n~~~~~~~~~Saída de Dados~~~~~~~~")
print(nome)
print(idade)
print(altura)

print('\n~~~~~~~~~~Tipos de Variáveis~~~~~~~~')
print(tipo_nome)
print(tipo_idade)
print(tipo_altura)

print("\n~~~~~~~~~~Concatenação~~~~~~~~")
print(nome, "tem", idade, "anos e", altura, "de altura") 