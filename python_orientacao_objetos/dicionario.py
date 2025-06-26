import os 
os.system('cls')

pessoa = {
    'nome': 'Ana',
    'idade': 28,
    'cidade': 'São Paulo'
}

pessoa['idade'] = 22

pessoa['profissao'] = 'Engenheiro'

del pessoa['cidade']

print(pessoa)