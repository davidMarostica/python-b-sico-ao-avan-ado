# aula 1 - arquivos em python
# w = write
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Ola arquivo Python")

    import csv

with open("dados.csv", "w") as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    # csv = linhas e colunas, comma separated values
    writer.writerow(["Nome", "Idade"])
    writer.writerow(["Matheus", 33])
    writer.writerow(["Maria", 44])
    writer.writerow(["David", 42])

with open("imagem.jpg", "rb") as img:
    conteudo = img.read()
    '''
    print(conteudo)
    '''

   # aula 2 - open e close
arquivo = open("teste.txt", "w")
print(arquivo.closed)
arquivo.write("Escrevi e pronto...")
print(arquivo.closed)
arquivo.close()
print(arquivo.closed)

# open => abre o arquivo
# close => fecha o arquivo

# a gente realize operacoes com o with

# se nao utilizar ou se pegar codigo legado/antigo, checar se há o close