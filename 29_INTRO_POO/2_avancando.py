# aula 1 - atributos de classe e de instancia
class ContaBancaria:
    taxa_juros = 0.05

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def consultar_saldo(self):
        return f"Você tem R${self.saldo} de saldo!"


conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Maria", 10000)

print(conta1.consultar_saldo())

print(conta1.saldo)
print(conta2.saldo)

print(ContaBancaria.taxa_juros)

ContaBancaria.taxa_juros = 0.10

print(ContaBancaria.taxa_juros)
