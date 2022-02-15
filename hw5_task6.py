my_set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set2 = {10, 20, 3, 4, 50, 6, 70, 80, 9}
# add
my_set1.add(0)
# copy
my_set1.copy()
# difference
my_set1.difference(my_set2)
x = my_set1 - my_set2
# discard
my_set1.discard(15)
# intersection
my_set1.intersection(my_set2)
a = my_set1 & my_set2
# isdisjoint
my_set1.isdisjoint(my_set2)
# issubset
my_set1.issubset({4, 5, 6})
# issuperset
my_set1.issuperset(my_set2)
# pop
my_set1.pop()
# remove
my_set1.remove(1)
# symmetric_difference
my_set1.symmetric_difference(my_set2)
b = my_set1 ^ my_set2
# union
new_set1 = my_set1 | my_set2
new_set2 = my_set1.union(my_set2)
new_set3 = my_set1.union((100, 110, 120))
# update
my_set1.update(my_set2)
my_set1 |= my_set2
# intersection_update
my_set1.intersection_update(my_set2)
my_set1 &= my_set2
# difference_update
my_set1.difference_update(my_set2)
my_set1 -= my_set2
# symmetric_difference_update
my_set1.symmetric_difference_update(my_set2)
my_set1 ^= my_set2
# clear
my_set1.clear()
