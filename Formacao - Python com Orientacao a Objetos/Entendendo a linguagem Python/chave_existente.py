import os 
os.system('cls')

pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}

if 'nome' in pessoa:
    print('Existe essa chave aqui no dic!')
else:
    print('Não existe essa chave no dic!')