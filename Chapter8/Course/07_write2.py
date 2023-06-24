# 1.ouverture du fichier, en mode a
f = open('python.txt', 'a')
# 2.écriture du fichier
f.write('\nhello world')
# 3.rafraîchissement du contenu
f.flush()