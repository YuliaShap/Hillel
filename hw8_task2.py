def max_in_two_arg(x, y: int):  # пишем функцию, котрая находит максимум из двух аргументов
    return max(x, y)  # возвращаем максимальное значение из двух элементов


def max_in_three_arg(x, y, z: int):  # пишем функцию, котрая находит максимум из трех аргументов
    max_in_two = max_in_two_arg(x, y)  # назначаем переменную, которая равна максимальному значению из первой функции
    return max(max_in_two, z)  # возвращаем макимальное значение из значения первой функции и аргумента второй функции


x = int(input('Введите х: '))  # просим ввести х
y = int(input('Введите y: '))  # просим ввести у
z = int(input('Введите z: '))  # просим ввести z

print(max_in_three_arg(x, y, z))  # принтим, что вернула вторая функция
