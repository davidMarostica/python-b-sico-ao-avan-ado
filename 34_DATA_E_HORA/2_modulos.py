# aula 1 - parsing de strings para datas
from datetime import datetime, timedelta

data = datetime.strptime("25/12/2024", "%d/%m/%Y")

print(data)

data_hora = datetime.strptime("25/10/2015 14:30", "%d/%m/%Y %H:%M")

print(data_hora)

try:
    data_invalida = datetime.strptime("200/10/24", "%d/%m/%Y")
except ValueError as e:
    print(f"Erro ao converter data: {e}")