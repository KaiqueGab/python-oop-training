from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praça = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Laranja', 5.00, 'Médio')
prato_salada = Prato('Salada Caesar', 15.00, 'Salada com alface, croutons e molho Caesar')

restaurante_praça.adcionar_no_cardapio(bebida_suco)
restaurante_praça.adcionar_no_cardapio(prato_salada)

def main():
    restaurante_praça.exibir_cardapio
    
if __name__ == "__main__":
    main()