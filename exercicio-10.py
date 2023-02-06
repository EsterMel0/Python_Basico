'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
num1 = int(input("informe num1 --->"))
num2 = int(input("informe num2 --->"))
num3 = int(input("informe num3 --->"))

if (num1 >= num2 and num1 >= num3 and num2 >= num3):
  print("A ordem decrescente é: {}, {}, {}".format(num1, num2, num3))
elif (num1 >=num3 and num1>=num2 and num3>=num2):
 print("A ordem decrescente é: {}, {}, {}".format(num1, num3, num2))
elif (num2>=num1 and num2>=num3 and num1>=num3):
 print("A ordem decrescente é: {}, {}, {}".format(num2, num1, num3))
elif(num2>=num3 and num2>=num1 and num3>=num1):
 print("A ordem decrescente é: {}, {}, {}".format(num2, num3, num1))
elif(num3>=num2 and num3>=num1 and num2>=num1):
 print("A ordem decrescente é: {}, {}, {}".format(num3, num2, num1))
elif(num3>=num1 and num3>=num2 and num1>=num2):
 print("A ordem decrescente é: {}, {}, {}".format(num3, num1, num2))  