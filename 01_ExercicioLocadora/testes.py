from Models.ModeloCarro import ModeloCarro
from Models.Carro import Carro
from Models.Cliente import Cliente

modelo = ModeloCarro("picape", "manual", "gasolina", "chevrolet", "toro")
carro =Carro(
    categoria=modelo.categoria,
    transmissao=modelo.transmissao,
    combustivel=modelo.combustivel,
    marca=modelo.marca,
    modelo=modelo.modelo,
    ano="2020",
    placa="gft-123"
)

cliente = Cliente("Dalila", "03546555155", "MG2276741")

print(modelo)
print()
print(carro)

print(cliente)