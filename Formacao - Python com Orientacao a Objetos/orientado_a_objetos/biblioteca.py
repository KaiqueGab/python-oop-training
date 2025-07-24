from livros_1 import Livro

livro_biblioteca = Livro('Python para desenvolvedores', 'Samuel Developer', 2023)
print(f'\nAntes de emprestar (biblioteca): Livro disponivel? {livro_biblioteca}')
livro_biblioteca.emprestar_livro()
print(f'Depois de emprestar (biblioteca): Livro disponivel? {livro_biblioteca}\n')

ano_desejado = 2019
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_desejado)
print(f"Livros disponíveis em {ano_desejado}: {livros_disponiveis_ano}")