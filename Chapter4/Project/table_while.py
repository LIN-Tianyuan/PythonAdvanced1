i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(str(j) + " * " + str(i) + " = " + str(i*j) + "\t", end="")
        j += 1
    print()
    i += 1