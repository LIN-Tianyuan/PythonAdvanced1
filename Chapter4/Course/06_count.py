sentence = "Alex est vraiment très beau."
count = 0

for element in sentence:
    if element == 'a':
        count += 1

print("Il y a " + str(count) + " a dans la chaîne qui est comptée.")
