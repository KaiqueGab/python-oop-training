import os
from unidecode import unidecode  # pip install unidecode

os.system('cls')

try:
    nome = str(input('Qual o seu nome: '))

    print(30 * '=')
    dia_semana = str(input('\nQual o dia da semana: '))

    # remove espaços, acentos e deixa em minúsculo
    dia_semana_formatado = unidecode(dia_semana.strip().lower())

    if (dia_semana_formatado in ['sabado', 'domingo']):
        print(f'Olá {nome}, bom fim de semana! \n')
    else:
        print(f'Olá {nome}, boa semana! \n')
        

except ValueError:
    print('Erro! Preencha todos os campos corretamente com números válidos.\n')