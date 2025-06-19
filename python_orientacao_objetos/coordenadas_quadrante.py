import os 

os.system('cls')

def exibir_resultado():
    x = int(input('Me informe o valor do quadrante X: '))
    y = int(input('Me informe o valor do quadrante Y: '))

    if x > 0 and y > 0:
        print('\nVocê está no Primeiro Quadrante, os valores de x e y são maiores que zero')
    elif x < 0 and y > 0:
        print('\nVocê está no Segundo Quadrante, o valor de x é menor que zero e o valor de y é maior que zero')
    elif x < 0 and y < 0:
        print('\nVocê está no Terceiro Quadrante, os valores de x e y devem ser menores que zero')
    elif x > 0 and y < 0:
        print('\nVocê está no Quarto Quadrante, o valor de x é maior que zero e o valor de y é menor que zero')
    else:
        print('\nO ponto está localizado no eixo ou origem')


def main():
    exibir_resultado()

if __name__ == '__main__':
    main()
