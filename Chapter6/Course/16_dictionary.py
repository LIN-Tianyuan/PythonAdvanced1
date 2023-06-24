list = [99, 88, 77]
print(list[1])
# Créer un dictionnaire
stu_score = {"Leo": 99, "Laurent": 88, "Kevin": 77}
print(stu_score["Laurent"])
print(stu_score["Kevin"])

# ajouter
stu_score["Lucas"] = 66
print(stu_score)
print("----------")
# modifier
stu_score["Laurent"] = 80
print(stu_score)
print("----------")
# supprimer
stu_score.pop("Laurent")
print(stu_score)
print("----------")
# supprimer tous
# stu_score.clear()
# print(stu_score)
# print("----------")
# obtenir tous les keys
keys = stu_score.keys()
print(keys)


print("----------")
stu_score2 = {
    "Leo": {"anglais": 85, "physique": 88, "math": 78},
    "Laurent": {"anglais": 86, "physique": 85, "math": 88},
    "Kevin": {"anglais": 75, "physique": 58, "math": 68}
}

print(stu_score2["Leo"])
print(stu_score2["Leo"]["physique"])

stu_score3 = {"Leo": 99, "Laurent": 88, "Kevin": 77}
# Itération dans la dictionnaire
keys = stu_score3.keys()
for key in keys:
    print(f"Nom:{key} Note:{stu_score3[key]}")