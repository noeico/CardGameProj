
my_set = {1,2,3,4,5}
my_set2 = {2,3,4,5,6}
print(my_set)
my_set.add(6)
print(my_set2)
my_set.remove(2)
print(my_set)
merge_set = my_set | my_set2
print(merge_set)
intersection_set = my_set & my_set2
print(intersection_set)
different_set = my_set - my_set2
print(my_set)
print(my_set2)
print(different_set)
print (3 in my_set)
my_set.discard(10)
print(my_set)