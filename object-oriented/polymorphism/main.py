import os
from carro import Carro

carro1 = Carro("Fusca", "Volkswagen", "azul")
carro2 = Carro("Civic", "Honda", "preto")
carro3 = Carro("Model S", "Tesla", "branco")



def main():
    os.system('cls')

    print(carro1)
    print(carro2)
    print(carro3)

    print(carro1.ligar())

if __name__ == '__main__':
    main()