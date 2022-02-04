print('Hello!')
nickname = input('Введите свой никнейм')
if nickname == 'admin':
    print('Привет, повелитель!')
gender = input('Введите свой пол')
age = int(input('Введите свой возраст'))
if nickname == 'Женя':
    print('Советую Вам посмотреть "TENET"', sep='', end='\n')
elif ((10 < age < 14 and gender == 'М') or (age > 30 and gender == 'М')):
    print('Советую Вам посмотреть "StarWars" или "Мандалорец"', sep='', end='\n')
elif 22 < age < 32 and gender == 'Ж':
    print('Советую Вам посмотреть "Трансформеры"', sep='', end='\n')
elif age < 16 and gender == 'Ж':
    print('Советую Вам посмотреть "Инсургент"', sep='', end='\n')
elif age > 11 and gender == 'М':
    print('Советую Вам посмотреть "TMNT"', sep='', end='\n')
if nickname == 'Guido':
    print('Огромное спасибо!', sep='', end='\n')
