# coding=utf-8
def devis(a, b):  
    assert b != 0, 'Нельзя делить на 0' 
    return a / b


def my_new_reduce(function, iterable, start=None):  
    it = iter(iterable) 
    if start is None:  
        value = next(it)  
    else:
        value = start  
    for element in it:  
        value = function(value, element)  
    return value  


x = my_new_reduce(devis, [110, 1, 10, 4])  
print(x)  
