"""Вернуть из dictionary все уникальные values.
Пример
Входные данные = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                  {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Результат = {'S001', 'S005', 'S007', 'S002', 'S009'}
Усложнение! +5 points
Вернуть ту же структуру.
После dictionary L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S005"}, {"V":"S009"},{"VIII":"S007"}]"""

list_with_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                 {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

res = {}
for diction in list_with_dict:
    for k, v in diction.items():
        if v not in res.values():
            res[k] = v
print(res)
