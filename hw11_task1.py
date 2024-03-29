def generator_function():  # создаем функцию
    for i in range(10):  # в цикле идем по всем элементам от 0 до 9
        yield i  # создаем генератор


for item in generator_function():  # идем в цикле по всем значениям в генераторе
    print(item)  # и принтим эти значения

generator_function()  # вызываем результат функции

##################################################################

# создаем функцию, которая считает арифм.прогрессию с аргументами старт, шаг, длина
def arifm_progr(a, b, length):
    count = 1  # счетчик
    while count <= length:  # идем в цикле пока счетчик меньше либо равен длины
        yield a  # создаем генератор
        a += b  # увеличиваем начальное значение на шаг
        count += 1  # увеличиваем счетчик на 1


for elem in arifm_progr(1, 2, 10):  # в цикле идем по всем элементам результата функции
    print(elem)  # принтим каждый элемент

#####################################################################
my_list = ['I', 'am', 'Python', 'Developer']  # создаем список


def list_items():  # создаем функцию
    for item in my_list:  # которая в цикле идет по всем значениям в списке
        yield item  # создаем генератор


gen = list_items()  # создаем переменную, в которой лежат результаты функции

iter = 0  # счетчик

while iter < len(my_list):  # чтобы не вылезла ошибка StopIterration, идем в цикле пока счетчик меньше длины списка
    print(next(gen))  # принтим каждый следующий элемент генератора
    iter += 1  # счетчик увеличиваем на 1

#############################################################
