# aula 1 - iterador

iterador = iter([1, 2, 3])

print(iterador)
print(next(iterador))
print(next(iterador))
print(next(iterador))
# print(next(iterador)) StopIteration erro

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.contador = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        raise StopIteration
    

contador = Contador(5)

for numero in contador:
    print(numero)


string = "Python"
string_iterador = iter(string)

print(next(string_iterador))
print(next(string_iterador))
print(next(string_iterador))

# verificar se algo é iteravel
from collections.abc import Iterable

print(isinstance([1,2 ,3], Iterable))
print(isinstance(123, Iterable))


# aula 2- geradores
def numeros():
    yield 1
    yield 2
    yield 3

for numero in numeros():
    print(numero)


def pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print(list(pares(15)))


def contador_infinito():
    i = 1
    while True:
        yield i
        i += 1


cont = contador_infinito()

print(next(cont))
print(next(cont))
print(next(cont))
print(next(cont))
print(next(cont))
print(next(cont))

def mensagens():
    yield "Olá"
    yield "Bem-vindo"
    yield "Tudo bem?"
    yield "Tchau"

for msg in mensagens():
    print(msg)