import os
os.system('cls')

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #Método __init__ de inicializar o Construtor
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): #Método __str__ de pegar a localização do objetivo na memoria e trazer o valor em formato String
        return f'{self._nome} | {self._categoria}'

    def listar_restaurantes():
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categorial'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

#Instanciando os Objetos
restaurante_praca = Restaurante('Praça', 'Pizzaria')
restaurante_pizza = Restaurante('PizzaExpress', 'Italiana')

Restaurante.listar_restaurantes()