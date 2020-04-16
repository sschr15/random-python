from sys import argv

words = []

try:
    with open(argv[1]) as file:
        contents = file.readlines()
        for i in contents:
            words.append(i.split("\t")[1] + "\n")

    with open(argv[2], "w") as file:
        file.writelines(words)
except:
    print("Not enough parameters!")