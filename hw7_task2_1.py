def square(side: int):  # пишем функцию для квадрата с параметром для его стороны
    p = 4 * side  # вычисляем периметр квадрата
    d = side * 2 ** 0.5  # вычисляем диагональ квадрата
    s = side ** 2  # вычисляем площать квадрата
    res = (p, d, s)  # результатом будет кортеж из значений
    return res  # возвращаем результат


result = square(int(input("Введите сторону квадрата: ")))  # просим ввести длину стороны квадрата, применяем ее к функции
print(result)  # принтим результат после ввода
