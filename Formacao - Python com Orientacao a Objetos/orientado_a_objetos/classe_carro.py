import os

class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        os.system('cls')
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}.'

carro1 = Carro('Fiat', 'Argo', 'preto', 2022)
carro2 = Carro('Volkswagen', 'Jetta', 'Chumbo', 2025)

print(carro1)