class Pessoa:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

    def caminhar(self, quantidade_passos):
        print(f'{self.nome} está caminhando {quantidade_passos} passos.')

p = Pessoa(1, 'João', 30)
print(f'ID: {p.id}, Nome: {p.nome}, Idade: {p.idade}')
p.caminhar(10)