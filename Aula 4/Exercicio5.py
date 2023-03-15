class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

c = ContaBancaria('João', 1000)
c.depositar(500)
c.sacar(200)
print(f'Saldo final: {c.saldo}')