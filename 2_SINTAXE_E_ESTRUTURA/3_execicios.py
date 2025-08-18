#Execicio 5
# Enucuado: Esceva um programa que exiba na tela a mensagem "Olá, Mundo!".
# Exibe a mensagem na tela    
#eninciado: Escreva um programa que calcula a idade de uma pessoa com base no ano de nascimento fornecido pelo usuário.
#Descrição : o programa deve soliciar ano de nascimento do usuarío e converter 
# a ebtrada para um número inteiro, calcular idade atual considerando ano atual e 
# exibir a utilizando a função print. Utilize comentários para explicar cada etapa do código.

# EX1
print("Olá, Mundo!") 

# EX2
nome = input("Digite seu nome: ")
print("Olá, " + nome + " tudo bem? ")

# EX3
if 10 > 5:
    print("10 é maior que 5")

# EX4 
n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")

# Converte os numeros 'em testo' para 'float' e realiza a soma
soma = float(n1) + float(n2)
print("A soma é: ", soma)

# EX5
# Solicita o ano de nascimento do usuário
ano_nascimento = input("Digite o ano do seu nascimento: ")

# Converte a entrada para inteiro
ano_nascimento = int(ano_nascimento)

# Define o ano atual (você pode atualizar conforme necessário)
ano_atual = 2025

# Calcula a idade
idade = ano_atual - ano_nascimento

# Exibe a idade na tela
print("Sua idade é:", idade)