"""Написать функцию которая будет у пользователя брать python объект в любом виде и выводить все его
не магические методы в списке и написать декторатор который будет выводить колличество методов в объекте.
Похожую задачу мы уже решали. Можете взять решение из предыдущей. Но декоратор уже ваш полностью
func(tuple())
[count, index]

@methods_amount
[count, index]
2
"""

a = [m for m in dir(tuple) if not m.startswith('__')]


def foo():
    def foo2(b):
        b = len(a)
        print(b)

    return foo2


print(a)
foo()

