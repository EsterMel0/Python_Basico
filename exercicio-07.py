'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante
'''

letra = input("Informe a letra desejada: ")

if (
        letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
    print("é vogal")

else:
    print("é consoante")