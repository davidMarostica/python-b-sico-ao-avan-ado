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

# aula 2 - compilacao de regex

padrao = re.compile(r"\d{4}-\d{2}-\d{2}")

texto = "Data: 2021-09-10"

print(padrao.search(texto).group())

texto2 = "Data de ontem: 2021-09-09"
texto3 = "Data de amanhã: 2021-09-11"

print(padrao.search(texto2).group())
print(padrao.search(texto3).group())

padrao = re.compile(r"python", re.IGNORECASE)

texto4 = "Python"
texto5 = "PytHon"

print(bool(padrao.search(texto4)))
print(bool(padrao.search(texto5)))
