class Restaurante:
    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha

    def descreve_restaurante(self):
        print(f'Nome: {self.nome}, Tipo de Cozinha: {self.tipo_cozinha}')

    def abrir_restaurante(self):
        print('O restaurante está aberto.')

    def fechar_restaurante(self):
        print('O restaurante está fechado.')

r = Restaurante('Pizza Hut', 'Pizzaria')
print('Nome do Restaurante:', r.nome)
print('Tipo de Cozinha:', r.tipo_cozinha)
r.abrir_restaurante()
r.fechar_restaurante()

