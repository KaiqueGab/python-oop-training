import os
import random

os.system('cls')

try:
    nome = str(input('Qual o seu nome: '))
    numeroSecreto = random.randint(1, 50)
    numeroInputUser = None

    while numeroInputUser != numeroSecreto:
        print(30 * "=")
        numeroInputUser = int(input('\nMe informe um número (entre 1 a 50), torça para acertar: '))


        if (numeroInputUser < numeroSecreto):
            print(f"Olá {nome}, o numero é maior que o digitado, tente novamente!!! \n")

        elif (numeroInputUser > numeroSecreto):
            print(f"Olá {nome}, o numero é menor que o digitado, tente novamente!!! \n")

        else:
            print(f"Olá {nome}, voce acertou o Número SECRETO {numeroSecreto} \n")
        

except ValueError:
    print("Erro! Preencha todos os campos corretamente com números válidos.\n")