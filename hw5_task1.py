password_1 = input('Enter your password')  # просим ввести пароль и запоминаем его
password_2 = input('Enter your password again')  # просим ввести такой же пароль еще раз
if password_1 == password_2:  # если пароли совпали
    print('Welcome!')  # принтим сообщение
while password_1 != password_2:  # если пароли не совпали, задаем цикл пока они не совпадут
    print('Enter correct password')  # принтим сообщение ввести правильный пароль
    password_2 = input()  # ввод пароля
    if password_1 == password_2:  # если после цикла while они совпали
        print('Welcome!')  # принтим сообщение

