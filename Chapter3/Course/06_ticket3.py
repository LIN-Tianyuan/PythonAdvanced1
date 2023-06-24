print("Bienvenue au Zoo!")
if int(input("Veuillez indiquer votre taille (cm):")) > 120:
    print("Vous mesurez plus de 120cm et n'êtes pas autorisé à jouer gratuitement.")
    print("Cependant, si votre niveau VIP est supérieur à 3, vous pouvez jouer gratuitement.")
    if int(input("Veuillez entrer votre niveau VIP(1-5):")) > 3:
        print("Votre niveau vip est supérieur à 3 et vous pouvez jouer gratuitement.")
    else:
        print("Désolé, toutes les conditions ne sont pas remplies et un billet est nécessaire pour 10 euro.")
print("Bonne visite!")