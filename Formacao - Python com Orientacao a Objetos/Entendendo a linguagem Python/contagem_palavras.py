import os 
os.system('cls')

frase = "o rato roma roeu a roupa do rei de roma roma."
palavras = frase.split()

frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)