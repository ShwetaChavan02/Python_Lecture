# reading file without using readline

f = open("sample.txt", "r")

for line in f:
    print(line, end="")

f.close()