# Définition d'un tuple
t1 = (1, 2, "Hello", 3, 4, "Hello")
# Récupération des données par indice(index)
print(t1[2]) # Hello
# Trouver la première correspondance pour un élément
# spécifique basé sur index()
print(t1.index("Hello")) # 2
# Compter le nombre de fois qu'une donnée apparait
# dans un tuple
print(t1.count("Hello")) # 2
# Compter le nombre d'éléments dans un tuple
print(len(t1)) # 6

t2 = ((1, 2, 3), (4, 5, 6))
print(t2[0][0]) # 1
print(len(t2)) # 2

t3 = (1, 2, ['leo', 'laurent'])
print(len(t3)) # 3
t3[2][1] = 'lucas'
print(t3)

