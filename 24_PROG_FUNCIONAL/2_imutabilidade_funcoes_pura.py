# Aula 1 - Imutabilidade
dados = (1, 2, 3)

# listas nao sao imutaveis
original = [1, 2, 3]

nova_lista = [x + 1 for x in original]

print(original)
print(nova_lista)

#set = conjunto
conj = {1, 2, 3}

conj_frozen = frozenset(conj)

print(conj_frozen)

def adicionar(lista, el):
    return lista + [el]

nova_lista = adicionar(original, 100)

print(original)
print(nova_lista)

# aula 2 - funcoes puras
def eh_positivo(n):
    return n > 0


print(eh_positivo(12))
print(eh_positivo(-12))

def calcular_cubo(n):
    return n**3

print(calcular_cubo(12))

# Aula 3 - efeitos colaterais
# nao alterar o dado original
lista = [1, 2, 3]

def duplicar_elementos(lista):
    return [i * 2 for i in lista]

lista_dobrada = duplicar_elementos(lista)

print(lista_dobrada)

lista_dobrada_lambda = list(map(lambda x: x * 2, lista_dobrada))

print(lista_dobrada_lambda)

dict = {"nome": "Matheus", "idade": 33}

def adicionar_chave(dict, chave, valor):
    novo = dict.copy()
    novo[chave] = valor
    return novo

dict_novo = adicionar_chave(dict, "profissao", "Programador")

print(dict_novo)

contador = 0

def incrementador(valor):
    global contador
    novo_valor = contador + valor
    return novo_valor

num_novo = incrementador(10)

print(num_novo)

'''
graph TD
    A[Imutabilidade & Funções Puras] --> B[Imutabilidade]
    A --> C[Funções Puras]
    A --> D[Evitar Efeitos Colaterais]
    
    B --> B1[Estruturas Imutáveis]
    B --> B2[Técnicas de Transformação]
    B1 --> B1a[Tuplas, Strings, Números]
    B2 --> B2a[List Comprehensions]
    B2 --> B2b[Retornar Novas Estruturas]
    B2 --> B2c[Cópias vs Referências]
    
    C --> C1[Sem Efeitos Colaterais]
    C --> C2[Previsibilidade]
    C --> C3[Facilidade de Teste]
    
    D --> D1[Sem Modificação de Originais]
    D --> D2[Sem Dependência de Estado Externo]
    D --> D3[Uso Responsável de Globais]
    '''