grocery_list: list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']  # есть список продуктов
i = 0  # устанавливаем счетчик
while i <= len(grocery_list):  # пока счетчик меньше или равен длине списка
    for i in range(len(grocery_list)):  # идем по всем индексам списка
        if 'eg' in grocery_list:  # если eg есть в списке
            grocery_list.remove('eg')  # удаляем его из списка
            i += 1  # увеличиваем счетчик на 1
print(grocery_list)  # принтим оставшиеся элементы списка
