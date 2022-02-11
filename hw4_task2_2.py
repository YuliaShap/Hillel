your_string: str = str('Hillel school')
counter = 0
for i in your_string:
    for j in your_string:
        if i == j:
            counter += 1
        else:
            counter = 1
    print({i: counter}, end=' ')
