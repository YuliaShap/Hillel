your_list: list = list(input('Введите строку'))  # просим ввести строку, преобразовываем ее в список
new_dict = dict.fromkeys(your_list, 0)  # с помощью метода fromkeys создаем новый соварь из ключей списка, со значением по умолчанию 0
for key in your_list:  # в цикле перебираем ключи
    new_dict[key] += 1  # увеличиваем счетчик соответствующего ключа на 1
print(new_dict)  # принтим словарь
