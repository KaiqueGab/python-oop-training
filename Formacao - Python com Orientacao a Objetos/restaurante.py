import os
os.system('cls')

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): # Método __init__ de inicializar o Construtor
        self._nome = nome.title() # Usando a propriedade 'title()', toda primeira letra da palavra sera em Maiusculo
        self._categoria = categoria.upper() # Usando a propriedade 'upper()', todas as letras estarão em Maiusculo
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): # Método __str__ de pegar a localização do objetivo na memoria e trazer o valor em formato String
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    def alternar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

#Instanciando os Objetos
restaurante_praca = Restaurante('Praça', 'Pizzaria')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('PizzaExpress', 'Italiana')

Restaurante.listar_restaurantes()