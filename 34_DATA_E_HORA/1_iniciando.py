# aula 1 - manip. de data e hora

from datetime import datetime, timedelta, date, time

print(f"Data e hora atual: {datetime.now()}")

data_inicio = datetime.now()

data_consulta = data_inicio + timedelta(days=7)

print(data_consulta)

# aula 2 - datetime

data = date(2024, 5, 12)

print(data)

tempo = time(13, 33, 12)

print(tempo)

data_com_horario = datetime(2020, 10, 20, 14, 30, 10)
data_com_horario_2 = datetime(2021, 12, 24, 14, 30, 10)

print(data_com_horario)

diferenca = data_com_horario_2 - data_com_horario

print(diferenca)