class Livro():

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'{self._titulo} criado por {self._autor} no ano de {self._ano_publicacao}, Disponivel: {'Sim' if self._disponivel else 'Não'}'
    
    def emprestar_livro(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano_desejado):
        return [livro for livro in Livro.livros if livro._disponivel and livro._ano_publicacao == ano_desejado]
        # for livro in livros_disponiveis:
        #     return f'{livro._titulo} está disponível.'
