# try:
#     f = open('linux.txt', 'r')
# except:
#     f = open('linux.txt', 'w')

# try:
#     print(name)
# except NameError as e:
#     print("Erreur de nom de variable non définie.")

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(e)

# try:
#     print(1/0)
# except (NameError,ZeroDivisionError):
#     print("Erreur de ZeroDivision...")

# try:
#     print(name)
# except (NameError,ZeroDivisionError) as e:
#     print(e)

# try:
#     print(1)
# except Exception as e:
#     print(e)
# else:
#     print("Je suis else, le code qui exécuté quand il n'y a pas d'exception.")

# finally indique le code qui doit être éxécuté sans tenir compte des exception
try:
    f = open("test.txt", "r")
except Exception as e:
    f = open("test.txt", "w")
finally:
    f.close()