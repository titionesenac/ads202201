class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa('João', 30)
print(f'Nome: {p.nome}, idade: {p.idade}')