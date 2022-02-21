def season(month_number: int):  # назначаем функцию
    if month_number in range(3, 6):  # если месяц с 3 по 5
        return 'spring'  # возвращаем весна
    if month_number in range(6, 9):  # если месяц с 6 по 8
        return 'summer'  # возвращаем лето
    if month_number in range(9, 12):  # если месяц с 9 по 11
        return 'autumn'  # возвращаем осень
    if month_number in range(1, 3) or month_number == 12:  # если месяц с 1 по 2 или 12
        return 'winter'  # возвращаем зима


result = season(int(input("Введите номер месяца: ")))  # просим ввести номер месяца
print(result)  # принтим результат, который вернула функция

