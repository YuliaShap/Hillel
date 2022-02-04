year_of_birth = input('Hi! What is your year of birth?')  # просим ввести год рождения
actual_year = 2022                                         # указываем текущий год
if not year_of_birth.isdigit():                             # проверяем, являются ли введенные данные числом
    print('Insert the number')                              # если не число, просим его ввести
else:
    year_of_birth = int(year_of_birth)                      # преобразовываем введенные данные в число
    if actual_year - year_of_birth == 21:                   # если 21 год вывести “You should visit Holland.”
        print('You should visit Holland')
    elif actual_year - year_of_birth > 21:                  # если больше 21 вывести “You should visit Vietnam.”
        print('You should visit Vietnam')
    else:
        print('Travel everywhere')                          # все остальные варианты. Вывести “Travell everywhere”

