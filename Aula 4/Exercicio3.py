class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

r = Retangulo(5, 10)
print(f'Área do retângulo: {r.calcular_area()}')