method = dir(set)  # вызываем dir для set
method_list: list = list(map(str, method))  # преобразовываем список в список строк
counter = 0  # устанавливаем счетчик
while counter < len(method_list):  # пока счетчик меньше длины списка
    for i in range(len(method_list)):  # проходимся по каждому элементу списка
        while method_list[i].startswith('__') is True:  # если элемент начинается с '__'
            counter += 1  # счетчик увеличиваем на 1
            del(method_list[i])  # а найденый элемент удаляем
        break  # если не найдено элементов с __
    print(method_list)  # принтим оставшийся список
