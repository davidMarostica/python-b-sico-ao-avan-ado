# 1 - frozenset
print("Aula 1 - frozenset")
lista = [1, 2, 3, 4, 5]

fs = frozenset(lista)

print(fs)

# metodos de conj. geralmente funcionam em frozensets
fs2 = frozenset([4, 5, 6, 7])

print(fs.union(fs2))
print(fs.intersection(fs2))

# fs.add(x) -> erro

# fs.remove(2) -> erro

dicionario = {fs: "Teste"}

print(dicionario)
print()

# 2 - diferenças
print("Aula 2 -diferenças")
lista = [1, 2, 3, 4, 4]

conj = set(lista)

print(conj)

# intersecao de 2 listas
lista2 = [2, 3, 6, 7]

print(list(set(lista) & set(lista2)))

tupla = (1, 2, 3)

conj3 = set(tupla)

print(conj3)
print()