number = 5
num = int(input("Veuillez deviner un numéro: "))
if num == number:
    print("Félicitations, vous avez réussi du premier coup!")
elif int(input("Mauvaise réponse, encore une fois: ")) == number:
    print("Félicitations pour votre bonne réponse!")
elif int(input("Mauvaise réponse, encore une fois: ")) == number:
    print("Félicitations pour votre bonne réponse!")
else:
    print("Désolé, vous avez mal déviné. ")
