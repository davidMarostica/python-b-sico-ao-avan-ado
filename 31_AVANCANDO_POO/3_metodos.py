# aula 1 - metodos estáticos

class Validator:
    @staticmethod
    def validar_idade(idade):
        return idade > 0
    
print(Validator.validar_idade(10))
print(Validator.validar_idade(-5))

class Matematica:
    @staticmethod
    def soma(a, b):
        return a + b
    
    @staticmethod
    def calcular_area_retangulo(base, altura):
        return base * altura
    
    def soma2(self, a, b):
        return a + b
    

print(Matematica.soma(10, 2))

print(Matematica.calcular_area_retangulo(12, 5))

# print(Matematica.soma2(10, 2)) -> erro, precisa de objeto

# aula 2 - class methods

class ContaBancaria:
    total_contas = 0

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

        ContaBancaria.total_contas += 1

    @classmethod
    def obter_total_de_contas(cls):
        return cls.total_contas
    

print(f"Nós temos {ContaBancaria.obter_total_de_contas()} contas no banco!")

c1 = ContaBancaria("Matheus", 1000)
c2 = ContaBancaria("Pedro", 2000)
c3 = ContaBancaria("João", 3000)

print(f"Nós temos {ContaBancaria.obter_total_de_contas()} contas no banco!")
