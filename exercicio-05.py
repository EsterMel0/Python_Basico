'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
- calcule os descontos e o salário líquido, conforme a tabela abaixo:
'''
valor_por_horas = float(input(" informe quanto vc ganha por hora:"))
horas_trabalhadas = int(input(" informe as horas trabalhadas:"))

salario_bruto = (valor_por_horas * horas_trabalhadas)
inss = salario_bruto * 8/100
sindicato = salario_bruto * 5/100
descontos = inss + sindicato
salario_liq = salario_bruto - descontos

print("seu salario bruto é: %.2f" %salario_bruto)
print("foi pago ao inss: %.2f" %inss)
print(" valor pago ao sindicato: %.2f" %sindicato)
print("salario liquido: %.2f" %salario_liq)