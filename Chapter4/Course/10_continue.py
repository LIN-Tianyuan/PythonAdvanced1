for i in range(1, 5):
    print(f"Today is day {i}, Ready to confess my love.....")
    if input(f"Aujourd'hui Xiao Mei semble être de (0 bonne humeur, 1 mauvaise humeur)") == '1':
        print("Xiao Mei est de mauvaise humeur, je ne lui enverrai pas de fleurs aujourd'hui.")
        print()
        continue
    print("J'envoie des fleurs à Xiao Mei.")
    print()