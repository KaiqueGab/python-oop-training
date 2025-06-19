import os
import random

os.system('cls')

try:
    nome = str(input('Qual o seu nome: '))
    numero_secreto = random.randint(1, 50)
    numero_input_user = None

    while numero_input_user != numero_secreto:
        print(30 * "=")
        numeroInputUser = int(input('\nMe informe um número (entre 1 a 50), torça para acertar: '))


        if (numero_input_user < numero_secreto):
            print(f"Olá {nome}, o numero é maior que o digitado, tente novamente!!! \n")

        elif (numero_input_user > numero_secreto):
            print(f"Olá {nome}, o numero é menor que o digitado, tente novamente!!! \n")

        else:
            print(f"Olá {nome}, voce acertou o Número SECRETO {numero_secreto} \n")
        

except ValueError:
    print("Erro! Preencha todos os campos corretamente com números válidos.\n")