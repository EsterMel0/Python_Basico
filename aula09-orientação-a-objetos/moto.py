from veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, cor, marca, rodas, tanque):
        Veiculo.__init__(self, cor, marca, rodas, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print('Erro: Tanque cheio!')
        else:
            self.tanque += litros
            print('Abastecimento concluido!')