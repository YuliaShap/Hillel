# try/except
my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
except KeyError:
    print("That key does not exist!")

# try/finally
my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
except KeyError:
    print("That key does not exist!")
finally:
    print('Я всегда появляюсь в конце')

# raise
a = int(input())
b = int(input())
try:
    if b == 0:
        raise ZeroDivisionError
except:
    print('Деление на 0')

# assert
student_grades = [57, 74, 49, 0, 87, 66, 89]

for g in student_grades:
    assert student_grades[g] != 0
    if student_grades[g] >= 52:
        print('This student passed.')
    else:
        print('This student failed.')

print('Program complete')
