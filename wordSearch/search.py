from sys import argv

try:
    with open(argv[1]) as file:
        words = file.readlines()
    
    out = ""
    for i in words:
        if argv[2] in i:
            out += i
    
    if len(argv) > 3:
        with open(argv[3], "w") as file:
            file.write(out)
        print("Matches printed to " + argv[3])
    else:
        print(out)
except IndexError as ignored: 
    print("Not enough parameters!")