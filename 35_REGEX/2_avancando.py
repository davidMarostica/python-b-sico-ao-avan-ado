# aula 1 -  conjuntos
import re

texto = "Hoje é dia 20 de Janeiro de 2024"

print(re.findall(r"\d+", texto))

texto = "Python_3 é incrível!"

print(re.findall(r"\w+", texto))

texto = "Texto com espaços e \n quebras de \n linha"

print(re.findall(r"\s", texto))

texto = "abc 123 xyz"

print(re.findall(r"[a-c1-3]+", texto))


# aula 2 - quantificadores

print(re.findall(r"a*", "aaabaaca"))

print(re.findall(r"a+", "aaabaaca"))

print(re.findall(r"a?", "aaabaaca"))

print(re.findall(r"a{2,3}", "aaabaaca"))