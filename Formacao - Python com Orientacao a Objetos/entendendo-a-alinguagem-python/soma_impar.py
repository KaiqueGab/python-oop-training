import os
os.system('cls')

soma = 0

for num in range(1,11):
    print(num)
    if num % 2 != 0:
        soma = soma + num

print(f'\nA soma dos números impares foi {soma}')
