with open("word.txt", "r") as f:
    content = f.read()

count = content.count("alex")
print(f"alex appraît {count} fois dans le fichier word.txt.")