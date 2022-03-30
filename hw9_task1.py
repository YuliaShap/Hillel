def my_number(number: str):  # пишем функцию с аргументом number
    def user_telephone():  # вложенная функция
        print('+044' + number)  # которая принтит код +044 с аргументом number

    return user_telephone  # замыкаем функцию


my_number('838372893')()  # передаем аргумент и вызываем результат функции


