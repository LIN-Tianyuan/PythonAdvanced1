money = 5000000
name = input("Veuillez entrer votre nom:")

def query(show_header):
    if show_header:
        print("----------Vérifiez votre solde----------")
    print(f"{name}, bonjour, il vous reste un solde de {money} euros.")

def saving(num):
    global money
    money += num
    print("----------Dépôts----------")
    print(f"{name}, bonjour, votre dépôt de {num} euros a été accepté.")
    query(False)

def get_money(num):
    global money
    money -= num
    print("----------Retraits----------")
    print(f"{name}, bonjour, votre retrait de {num} euros a été effectué.")
    query(False)

def main():
    print("----------Menu principal----------")
    print(f"{name}, bonjour, bienvenue à ATM, veuillez sélectionner l'opération: ")
    print("Vérifier le solde\t[Entrer 1]")
    print("Dépôts\t\t\t\t[Entrer 2]")
    print("Retraits\t\t\t[Entrer 3]")
    print("Sortie\t\t\t\t[Entrer 4]")
    return input("Veuillez entrer votre choix: ")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("Combien voulez-vous économiser ? Veuillez entrer: "))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("Combien voulez-vous retirer ? Veuillez entrer: "))
        get_money(num)
        continue
    else:
        print("Sortie du programme!")
        break