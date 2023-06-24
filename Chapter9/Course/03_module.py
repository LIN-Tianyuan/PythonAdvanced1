"""
import time
print("Début")
# Mettre le programme en veille pendant 5 secondes
time.sleep(5)
print("Fin")


from time import sleep
print("Début")
sleep(5)
print("Fin")


# importation de toutes les méthodes du module temps
from time import *
print("Début")
sleep(5)
print("Fin")
"""

# Alias du module
import time as tt
tt.sleep(2)
print("hello")

# Alias de la fonction
from time import sleep as sl
sl(2)
print("hello")