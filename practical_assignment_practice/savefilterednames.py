# Save the filtered names (longer than 5 characters) into a new file. 

file = open("file.txt", "r")
students = file.read().splitlines()
file.close()

filtered = []

for name in students:
    if len(name) > 5:
        filtered.append(name)

new_file = open("filtered_names.txt", "w")

for name in filtered:
    new_file.write(name + "\n")

new_file.close()

print("Filtered names saved successfully")