# Aula 1 _ Métodos de string
texto = "python é muito legal"

print(texto.upper())  # "PYTHON É MUITO LEGAL"
print(texto.lower())
print(texto.title())  # "Python É Muito Legal"
print(texto.capitalize())  # "Python é muito legal"2    

# remocao de espaço
espacos = " teste aqui de python  "
print(espacos.strip())  # "teste aqui de python"
print(espacos.lstrip())  # "teste aqui de python  "
print(espacos.rstrip())  # " teste aqui de python"

# substituicao de caracteres
print(espacos.replace("python", "php "))  # " teste 2 aqui de python  "

dados = "nome, telefone, idade, endereco"

dados_separados = dados.split(", ")
print(dados_separados)  # ['nome', 'telefone', 'idade', 'endereco']

# Aula 2 split
frase = "Python é muito divertido e Python é uma linguagem poderosa."

lista_frases = frase.split()
print(lista_frases [1])  
string_caracteres = "teste_testando_testou"

print(string_caracteres.split("_"))  # ['teste', 'testando', 'testou']

print(frase.split(" ", 2)) 

# Aula 3 - join
palavras = ["Python", "é", "uma", "linguagem", "de", "programação"]

print(" ".join(palavras))  # "Python é uma linguagem de programação"

print(" , ".join(palavras))  # "Python - é - uma - linguagem - de - programação"

numeros = ["1", "2", "3", "4", "5"]

# map -> percorre uma lista, e modificar eles 
print(" - ".join(map(str, numeros)))  # "1 - 2 - 3 - 4 - 5"


# Aula 4 Replace
frase = "Python é uma linguagem de programação muito utilizada no mercado de trabalho."
print(frase.replace("Python", "Java"))  # "Java é uma linguagem de programação muito utilizada no mercado de trabalho."

palavras = "maçã laranja mação maçã"

print(palavras.replace("maçã", "banana", 2 ))  # "banana laranja mação banana"

#limpoar caracteres especiais
texto = "Sei lá @ teste !"

print(texto.replace("@", "").replace("!", ""))  # "Sei lá  teste "

print(texto)