# aula 1 - regex
import re

texto = "O número 422 está aqui."

resultado = re.search(r"\d+", texto)

print(resultado.group())

frase = "Python é muito legal!"

nova_frase = re.sub(r"legal", "massa", frase)

print(nova_frase)
