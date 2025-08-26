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