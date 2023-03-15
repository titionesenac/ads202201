class Pessoa(object):

    # __init__ é o constrututor da classe
    def __init__(self, nome, idnumero):
        self.nome = nome
        self.idnumero = idnumero

    def mostrar(self):
        print(self.nome)
        print(self.idnumero)

    def detalhe(self):
        print("Meu nome é {}".format(self.nome))
        print("Meu ID é : {}".format(self.idnumero))


# classe filho
class Empregado(Pessoa):
    def __init__(self, nome, idnumero, salario, endereco):
        self.salario = salario
        self.endereco = endereco

        # invocando o __init__ da classe pai
        Pessoa.__init__(self, nome, idnumero)

    def detalhe(self):
        print("Meu nome é {}".format(self.nome))
        print("Meu ID é : {}".format(self.idnumero))
        print("Endereço: {}".format(self.endereco))


# criação do do objeto atribuido a variável e inserindos valores nos atibutos
pessoaA = Empregado('Rahul', 886012, 200000, "Intern")

# chamando a função da classe Pessoa
pessoaA.mostrar()


