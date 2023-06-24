info_dict = {
    "Taylor": {
        "department": "Technology",
        "salary": 3000,
        "grade": 1
    },
    "Luna": {
        "department": "Market",
        "salary": 5000,
        "grade": 2
    },
    "Alex": {
        "department": "Market",
        "salary": 7000,
        "grade": 3
    },
    "Julien": {
        "department": "Technology",
        "salary": 4000,
        "grade": 1
    }
}

print(f"Résultats des employés avant une promotion et une augmentation de salaire: \n{info_dict}")
for name in info_dict:
    if info_dict[name]["grade"] == 1:
        info_dict[name]["salary"] += 1000
        info_dict[name]["grade"] += 1

print(f"Résultats des employés après une promotion et une augmentation de salaire: \n{info_dict}")