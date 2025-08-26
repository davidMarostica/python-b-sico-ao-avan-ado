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
