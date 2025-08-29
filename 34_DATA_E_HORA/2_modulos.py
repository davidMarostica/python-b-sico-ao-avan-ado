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

    # aula 2- calculo com datas

data1 = datetime(2024, 12, 25)
data2 = datetime(2025, 9, 12)

diferenca = data2 - data1

print(diferenca.days)

nova_data = data1 + timedelta(days=5)
nova_data_semanas = data1 - timedelta(weeks=3)

print(nova_data)
print(nova_data_semanas)

periodo = timedelta(days=3, hours=3)

data_evento = data1 + periodo

print(data_evento)