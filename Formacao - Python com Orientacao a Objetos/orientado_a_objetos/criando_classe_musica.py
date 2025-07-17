import os
os.system('cls')

class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'


musica1 = Musica('Under Pressure', 'Queen & David Bowie', 248)
musica2 = Musica('The Trooper', 'Iron Maiden', 245)
musica3 = Musica('Hotel California', 'Eagles', 390)

print(musica1)
print(musica2)