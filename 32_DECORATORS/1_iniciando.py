# aula 1 - introducao do modulo

# criar uma funcao
# @funcao

# decorators são reutilizaveis

def meu_decorador(funcao):
    def wrapper():
        print("Iniciando função...")
        funcao()
        print("Terminando funcao...")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Executando a função principal!")

minha_funcao()