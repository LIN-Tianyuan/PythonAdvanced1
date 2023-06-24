import random
num = random.randint(1, 100)

count = 0

while True:
    number = int(input("Veuillez saisir le numéro que vous souhaitez deviner: "))
    count = count + 1
    if number == num:
        print("Félicitations pour votre bonne réponse!")
        break
    elif number > num:
        print("Vous avez deviné un plus grand nombre.")
    else:
        print("Vous avez deviné un plus petit nombre.")

print("Vous avez deviné un total de " + str(count) + " fois!")
