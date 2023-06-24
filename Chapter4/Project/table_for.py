for element1 in range(1, 10):
    for element2 in range(1, element1+1):
        # print(str(element2) + ' * ' + str(element1) + " = " + str(element1 * element2) + "\t", end='')
        print(f"{element2} * {element1} = {element2 * element1} \t", end='')
    print()