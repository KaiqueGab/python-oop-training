class Restaurante:
    def __init__(self, nome, categoria): #Método de inicializar o Construtor
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self): #Método de pegar a localização do objetivo na memoria e trazer o valor em formato String
        return f'{self.nome} | {self.categoria}'

#Instanciando os Objetos
restaurante_praca = Restaurante('Praça', 'Pizzaria')
restaurante_pizza = Restaurante('PizzaExpress', 'Italiana')

restaurantes = [restaurante_pizza, restaurante_praca]

print(restaurante_praca)
print(restaurante_pizza)