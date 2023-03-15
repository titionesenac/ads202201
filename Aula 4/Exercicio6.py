class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def imprimir_informacoes(self):
        print(f'Título: {self.titulo}, autor: {self.autor}, ano: {self.ano}')

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

livro = Livro('TRe', 'pedro', 1987)

bib = Biblioteca()

bib.adicionar_livro(livro)

a = bib.livros[0]

print(a.ano)