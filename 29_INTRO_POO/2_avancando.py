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

# aula 3 - self

class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        resultado = a + b

        self.historico.append(f"Somar: {a} + {b} = {resultado}")

        return resultado
    
    def exibir_historico(self):
        return self.historico
    

calc = Calculadora()

print(calc.somar(10, 10))
print(calc.exibir_historico())

print(calc.somar(5, 12))
print(calc.somar(3, 20))
print(calc.exibir_historico())


# aula 4 - init

# init == funcao construtora

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

p1 = Pessoa("David", 42, "Programador")

print(p1.nome)

class Produto:
    def __init__(self, preco, nome="Produto Genérico"):
        self.nome = nome

        if preco < 0:
            raise ValueError("O preço nao pode ser negativo")

# new => Python n tem new
produto = Produto(10)

print(produto.nome)

try:
    produto2 = Produto(-5, "Cadeira")

    print(produto2.nome)
except ValueError as e:
    print(e)


