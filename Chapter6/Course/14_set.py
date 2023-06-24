name = {"Python", "666", "Python", "y6"}
print(name)

my_set = {"Leo", "Laurent"}
my_set.add("Kevin")
print(my_set)
print("--------------")
my_set.remove("Leo")
print(my_set)
print("--------------")
# Suppression aléatoire d'éléments d'un ensemble(set)
element = my_set.pop()
print(my_set)
print(element)
my_set.clear()
print(my_set)
print("--------------")
set1 = {1, 2, 3}
set2 = {1, 5, 6}
# Prend l'ensemble que l'ensemble 1 possède et que l'ensemble 2 ne possède pas
set3 = set1.difference(set2)
print(set1)
print(set2)
print(set3)
print("--------------")
# Comparer l'ensemble 1 et l'ensemble 2, dans l'ensemble 1, retirer les mêmes éléments
# que dans l'ensemble 2
set1.difference_update(set2)
print(set1)
print(set2)
print("--------------")
# Combiner la collection 1 et la collection 2
set4 = set1.union(set2)
print(set1)
print(set2)
print(set4)
# Compter le nombre d'éléments de l'ensemble
print(len(set4))
print("--------------")
for i in set4:
    print(i)