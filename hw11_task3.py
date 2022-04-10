# coding=utf-8
def devis(a, b):  # функция деления
    assert b != 0
    print('на ноль делить нельзя')
    assert a.isdigit() == True
    print('вы должны ввести число')
    assert b.isdigit() == True
    print('вы должны ввести число')
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


x = my_new_reduce(devis, [100, 1, 'hg', 1])  #
print(x)  #