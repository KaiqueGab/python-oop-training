class Livro():

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.ano_publicacao}) - Disponivel: {'Sim' if self.disponivel else 'Não'}"

    def emprestar_livro(self):
            self.disponivel = False
        
    def devolver_livro(self):
            self.disponivel = True

    @staticmethod
    def verificar_disponibilidade(ano_desejado):
        livros_disponiveis = [livro for livro in Livro.livros if livro.disponivel and livro.ano_publicacao == ano_desejado]
        for livro in livros_disponiveis:
            print(livro)


livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)

print(livro1)

livro1.emprestar_livro()
print(livro1)

Livro.livros = [livro1, livro2, livro3]

ano_especifico = 2019
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico) 
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")