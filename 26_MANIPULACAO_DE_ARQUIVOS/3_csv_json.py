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
    escritor.writerow(["David", "33", "Florianópolis"])
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

    escritor.writerow(["Elke", "50", "Rio de Janeiro"])

with open("produtos_teste.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter="/")

    escritor.writerows(dados)

with open("saida.csv", "a", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    escritor.writerow(["Elke", "50", "Rio de Janeiro"])

    # aula 3 - JSON
    import json

    dados = {"nome": "David", "idade": 42, "profissao": "Programador"}

    with open("dados.json", "w") as arquivo_json:
        json.dump(dados, arquivo_json)

usuarios = [
    {"nome": "David", "idade": 42, "profissao": "Programador"},
    {"nome": "Elke", "idade": 25, "profissao": "Medica"}
]

with open("usuarios.json", "w") as arquivo_json:
    json.dump(usuarios, arquivo_json)

    # aula 4- leitura json
with open("dados.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)

    print(dados['nome'])
    with open("usuarios.json", "r") as arquivo_json:
     usuarios = json.load(arquivo_json)
 
    for usuario in usuarios:
        print(usuario)
        print(f"Nome: {usuario['nome']} e Idade: {usuario['idade']}")

# ler 1 dado só -> n precisa loop
# ler varios dados -> lista -> aplicar um loop

# aula 5 - conversao de json e csv
with open("dados.csv", "r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)

    dados = list(leitor)

    print(dados)

    with open("dados_convertidos.json", "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

    with open("dados_convertidos.json", "r") as arquivo_json:
        dados = json.load(arquivo_json)   

    with open("dados_reconvertidos.csv", "w", newline="") as arquivo_csv:
         escritor = csv.DictWriter(arquivo_csv, fieldnames=dados[0].keys())

         escritor.writeheader()

         escritor.writerows(dados)
