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
