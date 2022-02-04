"""если на вводе убрать int, интерпретатор ругается на строчный age
 и отказывается с ним делать вычисления"""

age = int(input('Hi! What is your year of birth?')) #просим ввести именно число
if type(age) == str:    #зачем тогда эта проверка, если на входе int
    print('Insert the number')
elif 2022 - age == 21:
    print('You should visit Holland')
elif 2022 - age > 21:
    print('You should visit Vietnam')
else:
    print('Travel everywhere')
