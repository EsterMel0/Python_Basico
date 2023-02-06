class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite


    def depositar(self, valor1):
        self.saldo += valor1
        print('Depósito realizado com sucesso!!')


    def sacar(self, valor2):
        self.saldo -= valor2
        print("Saque realizado com sucesso!!")

