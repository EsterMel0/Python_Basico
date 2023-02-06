'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido
'''

while True:
    num = int(input("Informe um número:\n >> "))

    if num <= 10:
        print("Valor válido.")
        break
    else:
        print("Valor inválido. Tente novamente.\n")