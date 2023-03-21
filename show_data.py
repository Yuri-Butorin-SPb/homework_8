def printAll(path):
    data = open(path, 'r', encoding= "utf-8")
    for line in data:
        print(line)
    data.close()