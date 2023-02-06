from cliente import Cliente
from conta import Conta

cliente01 = Cliente('Ana', '000.000.000-00', 25)
print('\tCLIENTE 001')
print('NOME:\t', cliente01.nome)
print('CPF:\t', cliente01.cpf)
print('IDADE:\t', cliente01.idade, 'anos')

print("")

print('\tDADOS BANCÁRIOS')
conta01 = Conta(cliente01.nome, 0.0, 1000.0)
print('SALDO:\t', conta01.saldo)
print('LIMITE:\t', conta01.limite)
print("")
conta01.depositar(1000.0)
print('SALDO ATUAL:\t', conta01.saldo)




print("")
print(35*"-")
print("")

cliente02 = Cliente('João', '111.111.111-11', 32)
print('\tCLIENTE 002')
print('NOME:\t', cliente02.nome)
print('CPF:\t', cliente02.cpf)
print('IDADE:\t', cliente02.idade, 'anos')

print("")

print('\tDADOS BANCÁRIOS')
conta02 = Conta(cliente02.nome, 0.0, 1000.0)
print('LIMITE:\t', conta02.limite)
print("")
conta02.depositar(100.0)
print('SALDO ATUAL:\t', conta02.saldo)
conta02.depositar(200.0)
print('SALDO ATUAL:\t', conta02.saldo)

