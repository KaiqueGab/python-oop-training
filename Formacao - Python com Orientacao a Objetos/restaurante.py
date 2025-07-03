import os
os.system('cls')

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #Método __init__ de inicializar o Construtor
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): #Método __str__ de pegar a localização do objetivo na memoria e trazer o valor em formato String
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'Nome: {restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

#Instanciando os Objetos
restaurante_praca = Restaurante('Praça', 'Pizzaria')
restaurante_pizza = Restaurante('PizzaExpress', 'Italiana')

restaurantes = [restaurante_pizza, restaurante_praca]

print(restaurante_praca)
print(restaurante_pizza)