# File + List + String Combined Challenge o Read names from file → list.
# Remove duplicates.
# Sort by length (shortest to longest). 
# Write results into processed_names.txt 

f = open("file.txt", "r")
names = list(set(f.read().splitlines()))
f.close()

names.sort(key=len)

f = open("processed_names.txt", "w")

for name in names:
    f.write(name + "\n")

f.close()

print("Names saved successfully")