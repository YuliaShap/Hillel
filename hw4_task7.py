list_with_tuple: list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]  # получаем список кортежей
new_list = list(map(list, list_with_tuple))  # каждый кортеж в списке приобразовываем в список
print(new_list)  # выводим список списков