import os 
os.system('cls')

numeros = [10, 3, 6, 1]
soma = 0

try:
    for num in numeros:
        soma = soma + num
        print(num) 
    print((f'a soma dos numeros é {soma}'))
except Exception as e:
    print(f"Ocorreu um erro: {e}")