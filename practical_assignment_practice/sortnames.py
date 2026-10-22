# Sort the list of names alphabetically and print them in ascending order.

f = open("file.txt", "r")
names = f.read().splitlines()
f.close()

print(sorted(names))