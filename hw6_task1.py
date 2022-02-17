dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40}
dict_3 = {5: 50, 6: 60}
dict_4 = {7: 70, 8: 80}
dict_5 = {9: 90, 10: 100}
# решение с помощью распаковки
merged_dict1 = {**dict_1, **dict_2, **dict_3, **dict_4, **dict_5}
print(merged_dict1)

# решение с помощью цикла и метода items
merge_dict2 = {k: v for d in (dict_1, dict_2, dict_3, dict_4, dict_5) for k, v in d.items()}
print(merge_dict2)

