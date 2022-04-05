"""Функция reduce принимает 2 аргумента: функцию и последовательность.
reduce() последовательно применяет функцию-аргумент к элементам списка, возвращает единичное значение."""

from functools import reduce  # вызываем функцию reduce из модуля functools

items = [1, 24, 17, 14, 9, 32, 2]  # дан список из чисел

all_max = reduce(lambda a, b: a if (a > b) else b,
                 items)  # с помощью reduce и лямбда-функции находим максимальное число из списка

print(all_max)  # принтим максимальное число


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




# def my_new_reduce(function, items, value=0):
#     it_items = iter(items)
#     for item in it_items:
#         if item[0] > item[1]:
#             value = item[0]
#         else:
#             value = item[1]
#     return value


