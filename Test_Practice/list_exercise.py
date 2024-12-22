import random
my_list=[]
for x in range (10):
	my_list.append(x+1)
print(my_list)

new_list = []
length_my_list = len(my_list)
for x in range(3):
    new_list.append(my_list[length_my_list -1 - x])
print(new_list)

print(my_list[: :-1])
print(my_list[1::+2])

new_list2 = []
for x in range(5):
    new_list2.append(my_list[x])
print(new_list)

num1 = int(input("please insert a number"))
print(my_list)
my_list[-3:] = [num1]
print(my_list)

