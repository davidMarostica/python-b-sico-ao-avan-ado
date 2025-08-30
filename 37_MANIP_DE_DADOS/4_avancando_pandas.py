# =========================
# AULA 1 – Filtragem de Dados
# =========================
import pandas as pd

data_aula1 = {'Nome': ['Ana', "João", 'Maria'], 'Idade': [20, 32, 44]}
df_aula1 = pd.DataFrame(data_aula1)

# Filtro por idade
filtro_idade = df_aula1['Idade'] >= 30
print("Filtro idade >= 30:")
print(df_aula1[filtro_idade])

# Filtro por condição combinada
filtro_por_condicao = (df_aula1['Idade'] >= 20) & (df_aula1['Nome'] == 'Ana')
print("\nFiltro idade >= 20 e nome == Ana:")
print(df_aula1[filtro_por_condicao])

# Filtro com query
print("\nFiltro com query (Idade > 40 e Nome != 'Francisco'):")
print(df_aula1.query("Idade > 40 and Nome != 'Francisco'"))

# =========================
# AULA 2 – Operações Estatísticas
# =========================
df_aula2 = pd.DataFrame({'Categoria': ['A', 'A', 'B'], 'Valor': [10, 20, 30]})

print("\nResumo estatístico:")
print(df_aula2.describe())

print("\nMédia dos valores:", df_aula2['Valor'].mean())
print("Soma dos valores:", df_aula2['Valor'].sum())

grupo = df_aula2.groupby('Categoria')
print("\nSoma por categoria:")
print(grupo.sum())

print("\nAgregações por categoria (média e máximo):")
print(grupo.agg({'Valor': ['mean', 'max']}))

print("\nContagem por categoria:")
print(grupo['Valor'].count())

# =========================
# AULA 3 – Leitura de Arquivos e Banco de Dados
# =========================
# Criando dados fictícios e salvando como Excel
dados = {
    'ID': [1, 2, 3, 4, 5],
    'Nome': ['Ana', 'João', 'Maria', 'Carlos', 'Fernanda'],
    'Idade': [25, 30, 22, 28, 33],
    'Salário': [3000, 4000, 3200, 3500, 4500],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre'],
    'Experiência': [1, 1, 1, 2, 2]
}
df_aula3 = pd.DataFrame(dados)
df_aula3.to_excel('dados.xlsx', index=False)

# Leitura de arquivos
import os

try:
    if os.path.exists('dados.csv'):
        df_csv = pd.read_csv('dados.csv')
        print("\nConteúdo do CSV:")
        print(df_csv.head())
    else:
        print("\nArquivo dados.csv não encontrado.")
except Exception as e:
    print(e)

try:
    df_excel = pd.read_excel('dados.xlsx', engine='openpyxl')
    print("\nConteúdo do Excel:")
    print(df_excel.head())
except Exception as e:
    print("Erro ao ler dados.xlsx:", e)

try:
    if os.path.exists('dados.json'):
        df_json = pd.read_json('dados.json')
        print("\nConteúdo do JSON:")
        print(df_json.head())
    else:
        print("\nArquivo dados.json não encontrado.")
except Exception as e:
    print(e)

# Banco de dados SQLite
from sqlalchemy import create_engine

engine = create_engine("sqlite:///dados.db")

data_sql = {
    'ID': [1, 2, 3],
    'Nome': ['Ana', 'João', 'Paulo'],
    'Idade': [20, 30, 40],
    'Cidade': ['São Paulo', 'Floripa', 'Rio de Janeiro']
}
pd.DataFrame(data_sql).to_sql('tabela', con=engine, if_exists='replace', index=False)

try:
    df_sql = pd.read_sql('SELECT * FROM tabela', con=engine)
    print("\nConteúdo do banco SQLite:")
    print(df_sql.head())
except Exception as e:
    print("Erro ao ler do banco:", e)

# =========================
# AULA 4 – Exportação de Dados
# =========================
df_aula3.to_csv("saida.csv", index=False)
df_aula3.to_excel('saida.xlsx', index=False)
df_aula3.to_json('saida.json', orient='records', lines=True)

print("\nExportações concluídas com sucesso.")
