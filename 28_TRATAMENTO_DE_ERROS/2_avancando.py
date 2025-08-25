# aula 1 - finally
# finally precisa do try, mas nao precisa do except
try:
    arquivo = open("arquivo2.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo nao existe")
finally:
    try:
        arquivo.close()
        print("Fechou o arquivo")
    except NameError:
        print("O arquivo nunca fui aberto..")

try:
    resultado = 10/0
except ZeroDivisionError as e:
    print("Divisao por zero...")
    print(f"Msg de erro: {e}")
finally:
    print("A operação foi concluida!")

