year_of_birth = input('Hi! What is your year of birth?')
actual_year = 2022
if not year_of_birth.isdigit():
    print('Insert the number')
else:
    if actual_year - year_of_birth == 21:
        print('You should visit Holland')
    elif actual_year - year_of_birth > 21:
        print('You should visit Vietnam')
    else:
        print('Travel everywhere')
