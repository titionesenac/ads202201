class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def imprimir_informacoes(self):
        print(f'Marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}')

c = Carro('Ford', 'Fusion', 2015)
c.imprimir_informacoes()