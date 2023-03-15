
class CanecaCeramica:

    def __int__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Vazia'
    # O conteúdo acima evidencia que os atribuos serão do objeto instanciado e não da classe

    def encher(self):
        self.status = 'Cheia'


    def beber(self ):
        print(f'estou bebendo da caneca{caneca1.nome}')


caneca_1 = CanecaCeramica()
caneca_1.nome = "Copa"
caneca_1.cor = "Verde"
caneca_1.logo = "CBF"


print(caneca1.cor, caneca1.nome, caneca1.logo)
caneca1.beber()


class Dog:
    # atributo da classe
    classe_animal = "mamífero"

    # atributo da instância
    def __init__(self, nome):
        self.nome = nome


    def latir(self):
        print("Latindo")


cao1 = Dog("Caramelo")
cao2 = Dog("pit")

cao1.latir()








