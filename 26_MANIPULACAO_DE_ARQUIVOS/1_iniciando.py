# aula 1 - arquivos em python
# w = write (escreve, sobrescreve o conteúdo)

with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá arquivo Python")

import csv  # Importação deve estar fora do bloco 'with'

with open("dados.csv", "w", newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    # csv = linhas e colunas, comma separated values
    writer.writerow(["Nome", "Idade"])
    writer.writerow(["Matheus", 33])
    writer.writerow(["Maria", 44])
    writer.writerow(["David", 42])

with open("imagem.jpg", "rb") as img:
    conteudo = img.read()
    # print(conteudo)  # descomente se quiser ver os bytes da imagem

# aula 2 - open e close
arquivo = open("teste.txt", "w")
print("Antes do close:", arquivo.closed)
arquivo.write("Escrevi e pronto...")
print("Durante o uso:", arquivo.closed)
arquivo.close()
print("Depois do close:", arquivo.closed)

# aula 3 - modos de arquivos
with open("exemplo.txt", "r") as arquivo:
    print("Conteúdo atual:", arquivo.read())

with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Sobrescrevendo tudo!")

with open("exemplo.txt", "a") as arquivo:
    arquivo.write("\nIsso está depois do que já foi escrito...")

with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Sobrescrevendo tudo!")
