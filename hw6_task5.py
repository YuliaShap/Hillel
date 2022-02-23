list_with_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                 {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# вернуть {'S001', 'S005', 'S007', 'S002', 'S009'}
res = set()  # создаем пустой set
for diction in list_with_dict:  # проходимся циклом по словарям в списке
    for v in diction.values():  # проходимся циклом по значениям в словарях
        res.add(v)  # добавляем значение в множество, т.к. это set, в нем будут только уникальные элементы
print(res)  # принтим результат

# L = [{"V": S001"}, {"V": "S002"}, {"VI": "S005"}, {"V":"S009"},{"VIII":"S007"}]
res_key = []
res_val = []

for diction in list_with_dict:
    for k, v in diction.items():
        if v not in res_val:
            res_key.append(k), res_val.append(v)
new_list = [{k: v} for k, v in zip(res_key, res_val)]

print(new_list)
