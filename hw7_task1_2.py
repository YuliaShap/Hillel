def foo():
    pass


print(foo())
############################
def sum(x, y: int):
    return x + y


x = 5
y = 10
print(sum(x, y))
############################
def add(x: int, y=10):
    return x + y


result = add(2)
print(result)
#############################
def say_hello(name: str):
    return f'Hello, {name}!'


name = input('What is your name')
print(say_hello(name))
#############################
def circle(length):  #нужно найти диаметр круга, зная его длину
    r = length / 3.14
    d = 2 * r
    return d


length = int(input('Введите длину окружности: '))
print(f'Диаметр круга - {circle(length)}')
###############################
def func(ab: int):
    if ab > 10:
        return ab + 1
    else:
        return ab * ab


ab = int(input())
print(func(ab))




