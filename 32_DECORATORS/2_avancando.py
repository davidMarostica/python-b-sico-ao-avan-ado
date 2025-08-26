# aula 1 - multiplos decorators
def decorador1(func):
    def wrapper(*args, **kwargs):
        print("Executando decorator1")
        return func(*args, **kwargs)
    return wrapper

def decorador2(func):
    def wrapper(*args, **kwargs):
        print("Executando decorator2")
        return func(*args, **kwargs)
    return wrapper

@decorador2
@decorador1
def dizer_ola():
    print("Olá, tudo bem?")

dizer_ola()

# aula 2 - decoradores de classe

# adicionando metodos
def adicionar_metodo_novo(cls):
    def metodo_novo(self):
        return f"Este é um método novo na classe {cls.__name__}"
    cls.metodo_novo = metodo_novo
    return cls

@adicionar_metodo_novo
class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome

obj = MinhaClasse("Nome do Objeto")

print(obj.metodo_novo())

# alterar o comportamento de inicializacao
def decorador_classe(cls):
    class NovaClasse(cls):
        def __init__(self, *args, **kwargs):
            print("Inicializando a classe com comportamento diferenciado.")
            super().__init__(*args, **kwargs)
    return NovaClasse

@decorador_classe
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

p = Pessoa("Alice")

print(p.nome)
