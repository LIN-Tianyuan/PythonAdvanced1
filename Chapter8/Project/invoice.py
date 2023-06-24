f = open("bill.txt", "r")
fw = open("bill.txt.bak", "a")

for line in f:
    # Nettoyage des espaces au début et à la fin
    line = line.strip()
    # print(line)
    if line.split(",")[4] == 'test':
        continue
    fw.write(line)
    fw.write('\n')

f.close()
fw.close()