my_list = [1, 2, 3, 4, 5]
new_list1 = my_list[1:4]
print(new_list1)
new_list2 = my_list[1:]
print(new_list2)
new_list3 = my_list[:4]
print(new_list3)
new_list4 = my_list[::2]
print(new_list4)
new_list5 = my_list[3:1:-1]
print(new_list5)


my_tuple = (1, 2, 3, 4, 5)
new_tuple1 = my_tuple[:]
print(new_tuple1)
new_tuple2 = my_tuple[:1:-2]
print(new_tuple2)

my_str = "12345"
new_str1 = my_str[:4:2]
print(new_str1)
new_str2 = my_str[::-1]
print(new_str2)