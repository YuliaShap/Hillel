new_tuple: tuple = ('1', '2', '3')  # пишем кортеж
list_tuple = list(new_tuple)  # т.к. кортеж неизменяемый список, приобразовываем его в обычный список
list_tuple.remove('3')  # удаляем элемент '3'
new_tuple = tuple(list_tuple)  # преобразовываем список обратно в кортеж
print(new_tuple)  # выводим кортеж
