import os
os.system('cls')

try:
    nome = input("Qual o seu nome: ")
    idade = int(input("Qual a sua idade: "))

    if (idade >= 18):
        print(f"Olá {nome}, voce já pode tirar a sua habilitação! \n")

    else:
        print(f"Olá {nome}, voce não pode tirar a sua habilitaçã! Ainda possui {idade} anos e só pode tirar a habilitação com 18 anos \n")

except ValueError:
    print("Erro! Preencha todos os campos corretamente com números válidos.")