import datetime  # импортируем модуль datetime

now = datetime.datetime.now()  # присваеваем переменной текущие значения даты и времени
year = lambda x: x.year  # с помощью лямбда-функции извлекаем текущий год
month = lambda x: x.month  # текущий месяц
day = lambda x: x.day  # текущий день

print(year(now))  # принтим текущий год
print(month(now))  # текущий месяц
print(day(now))  # текущий год
