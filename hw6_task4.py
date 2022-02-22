diction = {'id1': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}},
           'id2': {'name': 'Mark', 'class': 2, 'subjects': {'Geometry', 'Java', 'Cooking'}},
           'id3': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}}}
res = {}  # создаем новый словарь
for k, v in diction.items():  # проходимся по всем ключам, значениям словаря
    if v not in res.values():  # если значения нет в новом словре
        res[k] = v  # записываем это значение, если попадется дубликат, цикл его скипнет
print(res)  # принтим результат
