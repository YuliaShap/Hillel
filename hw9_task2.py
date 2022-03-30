def my_decorator(function):  # пишем декоратор
    def wrapper(arg):  # функция обертки 
        func = function(arg)  # назначаем переменную для результатов функции
        res = len(func)  # считаем длину списка
        print(func)  # принтим результат декорироуемой функции
        print(res)  # принтим результат текоратора

    return wrapper  # возвращаем функцию обертки


@my_decorator  # декорируем функцию ниже
def no_magic_methods(obj):  # фуекция, которая выводит все немагические методы обьекта

    return [m for m in dir(obj) if not m.startswith('__')]  # листкомпрехеншен для определения немагических методов


no_magic_methods(tuple)  # вызываем функцию для объекта tuple
