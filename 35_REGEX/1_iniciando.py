# aula 1 - regex
import re

texto = "O número 422 está aqui."

resultado = re.search(r"\d+", texto)

print(resultado.group())

frase = "Python é muito legal!"

nova_frase = re.sub(r"legal", "massa", frase)

print(nova_frase)

# aula 2 - como funciona a regex

texto = "123 abc 456 abc 789 abc def jip kew"

print(re.findall(r"abc", texto))

print(re.findall(r"[a-e]+", texto))

# Python -> python => nao encontra

# PyThoN

texto = "Python é muito bom, python é muito legal, PyThOn é demais!"

print(re.findall(r"python", texto, re.IGNORECASE))
