# просим ввести список с числами
random_list: list = list(map(int, input('Введите произвольный список с числами').split(', ')))
counter = 0  # устанавливаем счетчик
while counter < len(random_list):  # в цикле идем по всем значениям, которые меньше длины списка
    if random_list[counter] % 2 == 0:  # если число четное
        counter += 1  # увеличиваем счетчик на 1
    elif random_list[counter] % 2 != 0:  # если число нечетное
        print('NO')  # принтим НЕТ
        break  # и обрываем цикл
else:  # если все числа четные и счетчик стал равен длине списка
    print('all numbers are even')  # принтим, что все числа четные
