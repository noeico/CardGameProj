

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
new_dic= {}
new_dic.update(dic1)
new_dic.update(dic2)
dic1.update(dic2)
print(new_dic)
print(8 in dic1)
reverse_dic = {value: key for key , value in dic1.items}