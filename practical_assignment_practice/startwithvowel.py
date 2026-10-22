# Count how many names start with a vowel 

file = open("file.txt", "r")

students = file.read().splitlines()

count = 0

for name in students:
    if name[0].lower() in "aeiou":
        count += 1

print("Names starting with a vowel: ", count)

file.close()