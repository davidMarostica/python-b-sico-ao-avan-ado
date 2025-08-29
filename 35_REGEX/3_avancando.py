# aula 1 - backreferences
import re

texto = "A palavra foo foo se se repete"

padrao = r"(\b\w+\b)\s+\1"

print(re.findall(padrao, texto))

texto = "1212 é um número valido"

padrao = r"(\d+)\1"

print(bool(re.search(padrao, texto)))

texto = "foo foo bar foo"

novo_texto = re.sub(r"(\b\w+\b)\s+\1", "", texto)

print(novo_texto)
