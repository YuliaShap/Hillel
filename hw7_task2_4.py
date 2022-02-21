def ispolindrom(my_string: str):  # назначаем функцию
    revers_string = my_string[::-1]  # определяем строку в обратном порядке
    if my_string == revers_string:  # если строки равны
        return True  # возвращаем True
    else:  # если нет
        return False  # возвращаем False


my_string = input("Введите строку: ")  # просим ввести строку

print(ispolindrom(my_string))  # принтим результат, который вернула функция
