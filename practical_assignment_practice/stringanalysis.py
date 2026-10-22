# String Analysis o For each name, print: ▪ Length of the name ▪ 
# First and last character ▪ Whether it is a palindrome

f = open("file.txt", "r")

for name in f:
    name = name.strip()
    print("Name:", name)
    print("Length:", len(name))
    print("First character:", name[0])
    print("Last character:", name[-1])
    print("Palindrome:", name == name[::-1])
    print()

f.close()