name = "Alex"
print(name[0]) # A
print(name[3]) # x
print(name[-1]) # x

name_string = "Leo and laurent"
# Trouver la valeur de l'indice
print(name_string.index("and")) # 4

new_name_string = name_string.replace("Leo", "Kevin")
# Remplacer toutes les chaînes de caractères dans
# la chaîne de caractères: chaîne1 par chaîne2
print(new_name_string) # Kevin and laurent

# Divise la chaîne de caractère en plusieurs chaînes de caractères
# selon la chaîne de séparation spécifiée
name_list = name_string.split(" ")
print(name_list)
print(type(name_list))

# Suppression des espaces avant et arrière
name_string = " Leo and laurent "
print(name_string.strip())

# Suppression de la chaîne spécifiée avant et après
name_string = "12Leo and laurent21"
print(name_string.strip("12"))

# Compter le nombre d'occurrences d'une chaîne de caractères
# dans une chaîne de caractères
name_string = "Jean-Lucas and Lucas"
print(name_string.count("Lucas"))
# Compter la longueur des chaînes de caractères
print(len(name_string))