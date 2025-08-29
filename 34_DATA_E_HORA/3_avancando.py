# aula 1 - datas recorrentes

import calendar

calendario = calendar.monthcalendar(2025, 2)

domingos = [semana[calendar.SUNDAY] for semana in calendario if semana[calendar.SUNDAY] != 0]

print(f"Domingos de {calendar.month_name[2]} 2025: {domingos}")



calendario_mes = calendar.monthcalendar(2024, 6)

print(calendario_mes)

calendar.setfirstweekday(calendar.SUNDAY)

calendario_mes_2 = calendar.monthcalendar(2024, 6)

print(calendario_mes_2)


for ano in range(2010, 2040):
    if calendar.isleap(ano):
        print(f"{ano} é bissexto")


        # aula 2 - pytz
import pytz
from datetime import datetime

zona_ny = pytz.timezone("America/New_York")
data_ny = datetime.now(zona_ny)

print(data_ny)

print(pytz.all_timezones[:100])

zona_br = pytz.timezone("America/Sao_Paulo")

data_br = datetime(2024, 2, 1, tzinfo=zona_br)

print(data_br)
