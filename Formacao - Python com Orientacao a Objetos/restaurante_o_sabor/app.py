from modelos.restaurante import Restaurante


restaurante_praça = Restaurante('Praça', 'Gourmet')

restaurante_praça.receber_avaliacao('Kaique', 5)
restaurante_praça.receber_avaliacao('Laiza', 2)
restaurante_praça.receber_avaliacao('akaw', 10)

restaurante_praça = Restaurante('Pizza', 'Pizzaria')

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()