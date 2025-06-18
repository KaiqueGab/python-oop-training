import os
from unidecode import unidecode  # pip install unidecode

os.system('cls')

try:
    nome = str(input('Qual o seu nome: '))

    print(30 * '=')
    diaSemana = str(input('\nQual o dia da semana: '))

    # remove espaços, acentos e deixa em minúsculo
    diaSemanaFormatado = unidecode(diaSemana.strip().lower())

    if (diaSemanaFormatado in ['sabado', 'domingo']):
        print(f'Olá {nome}, bom fim de semana! \n')
    else:
        print(f'Olá {nome}, boa semana! \n')
        

except ValueError:
    print('Erro! Preencha todos os campos corretamente com números válidos.\n')