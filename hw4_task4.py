name: str = input('Введите свое имя')  # просим ввести имя
upper_name = name.upper()  # приводим имя к верхнему регистру
lower_name = name.lower()  # приводим имя к нижнему регистру
print('{} {}'.format(upper_name, lower_name))  # выводим имя в верхнем и нижнем регистре
