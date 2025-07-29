from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praça = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Laranja', 5.00, 'Médio')
prato_salada = Prato('Salada Caesar', 15.00, 'Salada com alface, croutons e molho Caesar')

def main():
    print(bebida_suco)
    print(prato_salada)
    
if __name__ == "__main__":
    main()