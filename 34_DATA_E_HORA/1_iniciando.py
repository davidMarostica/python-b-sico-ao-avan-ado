# aula 1 - manip. de data e hora

from datetime import datetime, timedelta, date, time

print(f"Data e hora atual: {datetime.now()}")

data_inicio = datetime.now()

data_consulta = data_inicio + timedelta(days=7)

print(data_consulta)
