# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

data = datetime.now(timezone('asia/tokyo'))
print(data)

# data_str_data = '2024-05-06 07:49:23'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime(2024, 5, 6, 13, 29, 48)
# data = datetime.strptime(data_str_data, data_str_fmt)