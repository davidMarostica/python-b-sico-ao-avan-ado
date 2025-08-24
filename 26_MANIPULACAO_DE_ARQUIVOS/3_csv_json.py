import csv

# aula 1 - leitura de csv
with open("dados.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)

    for linha in leitor:
        print(linha)

with open("exemplo_csv.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=";")

    for linha in leitor:
        print(linha)

# pular o cabeçalho
with open("dados.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)

    next(leitor)

    for linha in leitor:
        print(linha)

# transformar em dicionario
with open("dados.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)

    cabecalho = next(leitor)

    dados = [dict(zip(cabecalho, linha)) for linha in leitor]

    print(dados)