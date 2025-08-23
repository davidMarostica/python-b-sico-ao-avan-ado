# aula 1- funcao lambda

soma = lambda a,b: a + b

print(soma(4, 5))

# sorted -> lambda, lista

strings = ["banana", "abacate", "limão"]

ordenado = sorted(strings, key=lambda x: len(x))

print(ordenado)

# lambda argumentos: expressao

# Aula 2- Map
numeros = [2, 4, 6, 8]

dobro = list(map(lambda x: x * 2, numeros))

print(dobro)

celsius = [0, 12, 35, 22]

fahrenheit = list(map(lambda temp: temp * 9/5 + 32, celsius))

print(fahrenheit)

palavras = ["ola", "python", "teste", "testando", "mais um teste"]

# ola => Ola

capitalizadas = list(map(lambda palavra: palavra.capitalize(), palavras))

print(capitalizadas)

# Aula 3 - Filter
numeros = [-10, -5, 1, 2, 3, 4, 5, 6, 7]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)

strings_grandes = list(filter(lambda palavras: len(palavras) > 7, palavras))

print(strings_grandes)

positivos = list(filter(lambda num: num >= 0, numeros))

print(positivos)

# aula 4 - Reduce
from functools import reduce

soma_total = reduce(lambda x, y: x + y, numeros)

print(soma_total)

maior_valor = reduce(lambda x, y: x if x > y else y, numeros)

print(maior_valor)

frase = reduce(lambda x, y: x + " " + y, palavras)

print(frase)

# aula 5- combinacao de map filter e reduce

# quando eu encadeio esses metodos, n precisamos do list
pares = filter(lambda x: x % 2 == 0, numeros)

print(pares)
#print(list(pares))

quadrados = map(lambda y: y ** 2, pares)

print(quadrados)
#print(list(quadrados))

soma_quadrados = reduce(lambda x, y: x + y, quadrados)

print(soma_quadrados)

'''
graph TD
    A[Funções Lambda & Ordem Superior] --> B[Função Lambda]
    A --> C[Map]
    A --> D[Filter]
    A --> E[Reduce]
    A --> F[Combinações]
    
    B --> B1[Funções anônimas]
    B --> B2[Sintaxe concisa]
    
    C --> C1[Transformação]
    C --> C2[Aplica função a todos elementos]
    
    D --> D1[Filtragem]
    D --> D2[Seleção por condição]
    
    E --> E1[Redução]
    E --> E2[Agregação para valor único]
    
    F --> F1[Pipeline de dados]
    F --> F2[Filter -> Map -> Reduce]
    '''