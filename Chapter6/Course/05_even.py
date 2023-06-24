list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list1 = []
new_list2 = []

for element in list:
    if element % 2 == 0:
        new_list1.append(element)

i = 0
while i < len(list):
    if list[i] % 2 == 0:
        new_list2.append(list[i])
    i = i + 1

print(f"Une boucle for retire les numéro pairs de la liste {list}"
      f" et forme une nouvelle liste {new_list1}.")

print(f"Une boucle while retire les numéro pairs de la liste {list}"
      f" et forme une nouvelle liste {new_list2}.")
