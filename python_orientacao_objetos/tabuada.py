import os
os.system('cls')

numero = int(input('Digita um número para verificar sua tabuada: '))

for mult in range (0, 11):
    multiplicacao = numero * mult
    print (f'A multiplicação do número {numero} x {mult} é {multiplicacao}\n')