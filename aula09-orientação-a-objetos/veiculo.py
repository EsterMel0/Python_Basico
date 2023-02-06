class Veiculo:

    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor # a cor do obj agora é o que eu definir
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros