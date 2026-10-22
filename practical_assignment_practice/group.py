# Read names from file. 
# Group them by starting letter (e.g., all names starting with A together). 
# Save each group into separate files (A_names.txt, B_names.txt, etc.).

f = open("file.txt", "r")
names = f.read().splitlines()
f.close()

groups = {}

for name in names:
    letter = name[0].upper()

    if letter not in groups:
        groups[letter] = []

    groups[letter].append(name)

for letter in groups:
    f = open(letter + "_names.txt", "w")

    for name in groups[letter]:
        f.write(name + "\n")

    f.close()

print("Files created successfully")