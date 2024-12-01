dataFile = open("WileyGAAP2020.txt", 'r', encoding="utf-8")
for line in dataFile:
    print(line.rstrip())
dataFile.close()
