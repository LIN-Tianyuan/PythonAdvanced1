import random
num = random.randint(1, 10)

number = int(input("Veuillez saisir le numéro que vous souhaitez deviner: "))
if number == num:
    print("Félicitations, vous avez réussi du premier coup!")
else:
    if number > num:
        print("Vous avez deviné un plus grand nombre.")
    else:
        print("Vous avez deviné un plus petit nombre.")
    number = int(input("Veuillez saisir le numéro que vous voulez deviner à nouveau: "))
    if number == num:
        print("Félicitations pour votre bonne réponse!")
    else:
        if number > num:
            print("Vous avez deviné un plus grand nombre.")
        else:
            print("Vous avez deviné un plus petit nombre.")
        number = int(input("Veuillez entrer le numéro que vous voulez deviner une troisieme fois: "))
        if number == num:
            print("Félicitations, dernière chance, vous l'avez deviné!")
        else:
            print("Les trois chances sont épuisées, vous n'avez pas deviné et le jeu a échoué.")