age = 31
year = 1
level = 1
if age < 18:
    print("Vous n'êtes pas un adult.")
elif age < 30:
    print("Adultes, continuez à juger.")
    if year > 2:
        print("Vous pouvez recevoir un cadeau.")
    elif level > 3:
        print("Vous pouvez recevoir un cadeau.")
    else:
        print("Conditions pas remplis, Vous ne pouvez pas recevoir un cadeau.")
else:
    print("Vous êtes trop âgé.")
