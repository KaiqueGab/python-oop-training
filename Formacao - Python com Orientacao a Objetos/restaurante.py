class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('praça', 'pizzaria')
restaurante_pizza = Restaurante('PizzaExpress', 'Italiana')

restaurantes = [restaurante_pizza, restaurante_praca]

print(vars(restaurante_praca))
print(vars(restaurante_pizza))