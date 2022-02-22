# list comprehension
squares = [x * x for x in (1, 2, 3, 4)]
upper_let = [x.upper() for x in "Python Developer"]
odd = [x for x in range(10) if x % 2 != 0]
matrix = [[x for x in range(1, 5)] for y in range(1, 5)]
merge_list = [x for y in zip(list1, list2) for x in y]

# dict comprehension
squares1 = {i: i * i for i in range(10)}
d = {num: num**2 for num in range(1, 11)}
my_dict = {'k1': 2, 'k2': 4, 'k3': 6}
new_dict = {k: v for (k, v) in my_dict.items() if v > 2 if v < 6}
key_upper = {k.upper(): v for (k, v) in my_dict.items()}
key_lower = {key.lower(): value for key, value in my_dict.items()}

# set comprehension
x = {s for s in [1, 2, 1, 0]}
y = {s**2 for s in [1, 2, 1, 0]}
z = {s**2 for s in range(10)}
a = {s for s in [1, 2, 3] if s % 2}
b = {(m, n) for n in range(2) for m in range(3, 5)}




