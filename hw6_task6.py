schedule = {'monday': ['clean house', 'drive car', 'meet with friends'],
             'tuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
counter = 0  # устанавливаем счетчик
diction = {k: v for k, v in schedule.items() if v is not None}  # перезаписываем словарь без None
for values in diction.values():  # идем по значениям словаря
    for i in values:  # идем по каждому элементу значения
        counter += 1  # увеличиваем счетчик на 1
print(counter)  # принтим количество элементов


"""у меня не получилось без перезаписи словаря, ниже код, котрым я пыталась пройти по существующему словарю,
но None не хотел заходить в цикл. Если покажешь как это сделать без перезаписи словаря, буду очень благодарна"""
# for values in diction.values():
#     for i in values:
#         if i is None:
#             continue
#         else:
#             counter += 1
# print(counter)







