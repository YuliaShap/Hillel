new_list: list = list(map(str, input('Введите список').split(', ')))  # просим ввести список, преобразовываем строку в список
set_list = set(new_list)  # преобразовываем каждый элемент списка в множество, чтобы найти уникальные элементы
sorted_list = sorted(set_list)  # сортируем множество
print(sorted_list)  # выводим отсортированный список уникальных элементов

