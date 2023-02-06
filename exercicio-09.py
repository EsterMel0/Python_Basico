'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

prod1 = float(input("Informe o valor do produto 1: "))
prod2 = float(input("Informe o valor do produto 2: "))
prod3 = float(input("Informe o valor do produto 3: "))

if prod1 < prod2 and prod1 < prod3:
  print("Compre o produto 1.")

elif prod2 < prod1 and prod2 < prod3:
  print("Compre o produto 2.")

else:
  print("Compre o produto 3.")