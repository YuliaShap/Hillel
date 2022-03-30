def new_decorator(text):  # пишем новый декоратор с аргументом принимающим текст
    def my_decorator(function):  # внутри декоратор с аргументом принимающим функцию
        def wrapper(arg):  # функция обертки
            func = function(arg)  # назначаем переменную для результатов функции
            res = len(func)  # считаем длину списка
            print(func)  # принтим результат декорируемой функции
            print(text, res)  # принтим результат декоратора

        return wrapper  # возвращаем функцию обертки

    return my_decorator  # возвращаем функцию декоратора


@new_decorator('need to learn')  # декорируем функцию ниже с нужным нам текстом
def no_magic_methods(obj):  # функция, которая выводит все немагические методы обьекта

    return [m for m in dir(obj) if not m.startswith('__')]  # листкомпрехеншен для определения немагических методов


no_magic_methods(tuple)  # вызываем функцию для объекта tuple
