string = "fruit friend apple"
num = string.count("fr")
print(f"Il y a {num} caractères fr dans la chaîne fruit friend apple.")

new_string = string.replace(" ", "|")
print(f"La chaîne fruit friend apple est remplacée par un espace et le résultat est {new_string}.")

new_string_list = string.split(" ")
print(f"Le résultat de la division de la chaîne fruit friend apple par | est {new_string_list}.")