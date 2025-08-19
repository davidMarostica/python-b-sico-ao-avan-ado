# Aula 1 f strings
nome = "David"
idade = 30

print(f"Meu nome é {nome} e tenho {idade} anos.")  # "Meu nome é David e tenho 30 anos."

a = 5 
b = 10
print(f"A soma de {a} e {b} é {a + b}.")  # "A soma de 5 e 10 é 15."

valor = 12.9842754

print(f"O valor formatado é: {valor:.2f}")  # "O valor formatado é: 12.98"


# aula 2 format

print("Meu nome é {} e tenho {} anos.".format(nome, idade))  # "Meu nome é David e tenho 30 anos."

valor = 1.2345

print("O valor formatado é: {:.3f}".format(valor))  # "O valor formatado é: 1.235"

print("Ordem de parametros invertidas é: {1} e {0}".format("primeiro", "segundo"))  # "Ordem de parametros invertidas é: 30 e David"

# aula 3 Strings multiplas linhas
texto = """Essa é uma string
com múltiplas linhas.
Você pode escrever o que quiser aqui,
e ela manterá a formatação."""
print(texto)


texto2= '''Essa é outra string
com múltiplas linhas.
Você também pode usar aspas simples
para criar strings assim.'''
print(texto2)   

texto3 = """fiçõa teste 
não acita parametros e retorna 
valor 1"""

def teste():
    return 1 

nome = "David"

frase = f"""Meu nome é
{nome} 
tudo bem?"""
print(frase)  # "Meu nome é David tydo bem?"

texto_com_escape = """
qualquer coisa \n\n 
pulo linha"""
print(texto_com_escape)  # "qualquer coisa \n\n pulo linha"

# Aula 4 caracteres espciais
texto = "Testabci \n Caracteres |n Especiais"
print(texto)  # "Testabci \n Caracteres |n Especiais"

aspas = "e quero \"colcar \"aspas\" dentro da string"
print(aspas)  # "e quero \"colcar \"aspas\" dentro da string"

caminha_de_uma_pasta = r"C:\\Users\\David\\Documents\\Projeto"
print(caminha_de_uma_pasta)  # "C:\Users\David\Documents\Projeto"

texto_com_tab = "Texto com\ttabulação"
print(texto_com_tab)  # "Texto com	tabulação"