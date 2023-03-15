
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.id = 1

    def __str__(self):
        return self.nome

    # O método abaixo é um método de instancia, ou seja, ele só executa a ação proposta mediante a entrega de uma
    #   instância do objeto.
    def falar(self):
        print(f'A pessoa está falando')


    #O método estático é de escopo da classe, ou seja é acessível apenas através da classe, não da instância
    @staticmethod
    def verificar_pessoa(pessoa=None):
        if pessoa is None:
            print('Não existem pessoas')
        else:
            return pessoa


    #O método classmethod possibilita a instanciação de um novo objeto sem a necessidade de passagem pelo contrutor,
    #   como por exemplo quando precisar criar uma instância de pessoa e não possuir a idade dela,
    #   apenas ano de nascimento. No caso abaixo é necessário a passagem dos parâmetros nome e ano de nascimento
    #   para que seja instanciado um objeto python para que seja executado o retorno de uma instancia
    @classmethod
    def cria_por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


    #No caso abaixo, o método está atrleado a execução de uma ação, como na assinatura do método não pede nenhum
    # parâmetro, o método fica com acesso disponível sem a necessidade de instanciação de um objeto Pessoa.
    @classmethod
    def andar(cls):
        print('Pessoa andando')





pedro = Pessoa.cria_por_ano_nascimento("Pedro", 1978)
paulo = Pessoa('Paulo', 18)
fabio = Pessoa('Fabio', 17)
Pessoa.verificar_pessoa()

print(fabio.nome, fabio.idade)
print(paulo.nome, paulo.idade)
print(pedro.nome, pedro.idade)
a = 1

Pessoa.falar(paulo)
Pessoa.andar()
Pessoa.verificar_pessoa()




