my_list_with_tuple = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]  # список кортежей
sorted_list = sorted(my_list_with_tuple, key=lambda x: x[1])  # с помощью лямбда-функции сортируем кортежи по значениям второго элемента
print(sorted_list)  # принтим отсортированный список
