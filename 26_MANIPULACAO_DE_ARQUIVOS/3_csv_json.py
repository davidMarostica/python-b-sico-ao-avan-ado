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


   
   # aula 2 - escrita em csv
with open("saida.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    escritor.writerow(["Nome", "Idade", "Cidade"])
    escritor.writerow(["Matheus", "33", "Florianópolis"])
    escritor.writerow(["João", "40", "São Paulo"])

dados = [
    ["Produto", "Valor"],
    ["Cadeira", 100],
    ["Mesa", 500]
]

with open("produtos.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    escritor.writerows(dados)

with open("produtos_teste.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter="/")

    escritor.writerows(dados)

with open("saida.csv", "a", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    escritor.writerow(["Maria", "50", "Rio de Janeiro"])

with open("produtos_teste.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter="/")

    escritor.writerows(dados)

with open("saida.csv", "a", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    escritor.writerow(["Maria", "50", "Rio de Janeiro"])
