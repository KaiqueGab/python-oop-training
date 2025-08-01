from livros_1 import Livro

def main():
    livro_biblioteca1 = Livro("1984", "George Orwell", 1949)
    livro_biblioteca4 = Livro("pythonando", "George Orwell", 1949)
    livro_biblioteca2 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    livro_biblioteca3 = Livro('Python para desenvolvedores', 'Samuel Developer', 2023)

    Livro.livros = [livro_biblioteca1, livro_biblioteca2, livro_biblioteca3, livro_biblioteca4]

    for livro in Livro.livros:
        print(livro)

    print(f'\nAntes de emprestar (biblioteca): Livro disponivel? {livro_biblioteca3}')

    livro_biblioteca3.emprestar_livro()
    print(f'Depois de emprestar (biblioteca): Livro disponivel? {livro_biblioteca3}\n')

    ano_desejado = 1949
    livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_desejado)
    print(f"Livros lançados em {ano_desejado}:")
    for livro in livros_disponiveis_ano:
        print(livro)

if __name__ == "__main__":
    main()