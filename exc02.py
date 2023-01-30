'''
EXERCICIO 02: FAÇA UM PROGRAMA QUE PERGUNTE A IDADE, O PESO E A ALTURA DE UMA PESSOA E INFORME SE ELA ESTÁ 
APTA A ENTRAR NO EXERCITO.PARA ENTRAR É PRECISO TER MAIS DE 18 ANOS, PESO MAIOR OU IGUAL A 60KG E ALTURA 
MAIOR OU IGUAL A 1.70M.
'''

idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

if idade > 18 and peso >= 60 and altura >= 1.70:
  print("Voce está apto para servir.")
else:
  print("Voce não está apto para servir.")