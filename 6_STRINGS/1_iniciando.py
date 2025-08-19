linguagem = "Python" 
versao = "3.12"
teste = 'texto' 
testando = '''texto'''

print(linguagem, versao, teste, testando)

#Concatenação 
print("Esta é um curso de " + linguagem + " ele é muito completo!" + teste)

repeticoes = "Olá"  * 3 
print(repeticoes)

# 1 = é atribuição
# 2 = é comparação
print(1 == 2) # False
print(1 == 1) # True    

print(linguagem == "Python") # True
print(linguagem == "Java") # False

# qtb de caracteres
print(len("Algum texte")) # 11
print(len(linguagem)) # 6

# Defina a variável frase antes de usá-la
frase = "Python é uma linguagem de programação muito utilizada no mercado de trabalho."

# verificação se texto está contido em outro texto
print("Python" in frase) 
print("Java" in frase)

# Verificando se uma string está vazia
print(len(frase) == 0)

# aula 2 
palavra = "Python"
print(palavra[0])  # P
print(palavra[5])   # n
print(palavra[-1])  # n

try:
    print(palavra[6])  # Isso causará um erro, pois o índice 6 está fora do alcance
except IndexError:
    print("Índice fora do alcance da string.")  

    #começa com e ternina com 
    print(palavra.startswith("Py"))  # True
    print(palavra.endswith("on"))    # True     

    print(palavra.endswith("on"))  # True

    texto = "Esta é uma frase muito grande e longa"

    nova_frase = texto[10]

    print(nova_frase)  # a

    # aula 3 - fatiamento de strings
    frase = "Aprenda a programar em Python"
    subfrase = frase[:7]

    print(subfrase)  # Aprenda
    subfrase2 = frase[-6:]

    #fatiamento com passo
    subfrase3 = frase[::2]

