# aula 1- encapsulamento

# publico
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

pessoa = Pessoa("Alice")

print(pessoa.nome)

# protegido
class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def exibir_func(self):
        print(f"Nome: {self._nome} Salário: {self._salario}")


func = Funcionario("Paulo", 5000)

func.exibir_func()

# privados
class ContaBancaria():
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    def exibir_dados(self):
        print(f"Nome: {self.__nome} Saldo: {self.__saldo}")


conta = ContaBancaria("Pedro", 1000)

# print(conta.__nome) = erro

conta.exibir_dados()


# aula 2 - manipulacao de atributos com @property

class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_preco(self):
        return f"R${self.__preco}"
    
    def set_preco(self, preco):
        if preco < 0:
            print("O preço não pode ser negativo!")
            return
        self.__preco = preco

produto = Produto("Notebook", 4000)

print(f"Preço atual do produto: {produto.get_preco()}")

produto.set_preco(1000)

print(f"Preço atual do produto: {produto.get_preco()}")

# @property
class Carro:
    def __init__(self, modelo):
        self.__modelo = modelo

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo
    

carro = Carro("Civic")

print(carro.modelo)

carro.modelo = "Civic 2010"

print(carro.modelo)
