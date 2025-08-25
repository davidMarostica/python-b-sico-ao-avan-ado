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


# aula 2 - métodos
class Circulo:
    pi = 3.14

    @classmethod
    def area_com_raio(cls, raio):
        return cls.pi * (raio ** 2)
    
print(Circulo.area_com_raio(5))

class Conversor:
    @staticmethod
    def celsius_p_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    

print(Conversor.celsius_p_fahrenheit(10))
print(Conversor.celsius_p_fahrenheit(30))