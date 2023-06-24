for i in range(1, 5):
    print(f"Today is day {i}, Ready to confess my love.....")
    if input(f"Si vous êtes Mei, faites-moi savoir si vous me jetez explicitement"
             f"(0 pour regarder et observer à nouveau,"
             f"1 inapproprié pour rejeter).") == '1':
        print("Xiao Mei m'a rejeté, je ne poursuivrai plus Xiao Mei.")
        break
    print("J'envoie des fleurs à Xiao Mei.")
    print()