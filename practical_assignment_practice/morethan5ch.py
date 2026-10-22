# Print names longer than 5 characters.

file = open("file.txt", "r")

students = file.read().splitlines()

for name in students:
    if len(name) > 5:
        print(name)

file.close()