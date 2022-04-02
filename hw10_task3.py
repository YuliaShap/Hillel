def summa(a, b):  # пишем функцию деления
    try:
        a / b  # делим
    except (ZeroDivisionError) as e:  # ловим ошибку деления на ноль
        print("ай яй яй делить на ноль можно не многим")  # принтим сообщение
    except (ValueError) as e:  # ловим ошибку ValueError
        print('ValueError')  # принтим сообщение
    except (TypeError) as e:  # ловим ошибку TypeError
        print('TypeError')  # принтим сообщение
    finally:  # то, что отработает всегда
        print("I 'am happy that you learn python")  # принтим сообщение


summa(5, 0)  # вызываем функцию с аргументами
