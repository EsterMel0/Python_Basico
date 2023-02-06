from veiculo import Veiculo
from moto import Moto

carro1 = Veiculo('azul', 'fusca', 4, 10)
print("CARRO - 1")
print('Cor:', carro1.cor)
print('Marca:', carro1.marca)
print('Rodas:', carro1.rodas)
print('Tanque:', carro1.tanque)
carro1.abastecer(40)
print('Tanque:', carro1.tanque)

print("")

carro2 = Moto('preto', 'BMW', 2, 15)
print("MOTOCICLETA - 2")
print('Cor:', carro2.cor)
print('Marca:', carro2.marca)
print('Rodas:', carro2.rodas)
print('Tanque:', carro2.tanque)
carro2.abastecer(30)
print('Tanque:', carro2.tanque)