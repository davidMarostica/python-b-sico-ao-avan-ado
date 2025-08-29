# aula 1 - expressoes geradoras

exp_geradora = (x ** 2 for x in range(10))

print(list(exp_geradora))

print(sum(x ** 2 for x in range(6)))

lista = [i ** 2 for i in range(1000)]
gerador = (i ** 2 for i in range(1000))

import sys

print(f"Tamanho em bytes gerador: {sys.getsizeof(lista)} ")
print(f"Tamanho em bytes gerador: {sys.getsizeof(gerador)} ")