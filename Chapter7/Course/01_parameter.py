def user_info(name, age, gender):
    print(f"Votre nom est {name}, votre âge est {age} ans et votre sexe est {gender}.")

# Arguments positionnels
user_info("Alex", 18, "Homme")
# Arguments mot-clé
user_info(age=18, gender="Homme", name="Alex")
user_info("Alex", age=18, gender="Homme")
print("----------")
# Arguments par défaut
def user_info1(name, age, gender="Homme"):
    print(f"Votre nom est {name}, votre âge est {age} ans et votre sexe est {gender}.")
user_info1("Alex", 18)
user_info1("Luna", 18, "Femme")
print("----------")
# Arguments de longueur indéterminée
def user_info2(*args):
    print(args)

user_info2('Alex')
user_info2('Luna', 18)