# coding=utf-8
def devis(a, b):  # функция деления
    return a / b


def my_new_reduce(function, iterable, start=None):  # самописный reduce
    it = iter(iterable)  # создаем итератор
    if start is None:  #
        value = next(it)  #
    else:
        value = start  #
    for element in it:  #
        value = function(value, element)  #
    return value  #


x = my_new_reduce(devis, [100, 1, 1, 1])  #
print(x)  #

#################################################################
def my_reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
