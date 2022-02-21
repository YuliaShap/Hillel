def merge_lists(list1, list2: list):  # назначаем функцию
    return [x for y in zip(list1, list2) for x in y]  # идем по всем элементам х и y поочередно в двух списках и возвращаем их


list1 = [1, 2, 3]  # первый список
list2 = [11, 22, 33]  # второй список

print(merge_lists(list1, list2))  # принтим результат, который вернула функция
