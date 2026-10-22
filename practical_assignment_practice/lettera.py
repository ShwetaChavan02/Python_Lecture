# Print names that contain the letter "a"

f = open("file.txt", "r")
names = f.read().splitlines()
f.close()

for name in names:
    if "a" in name.lower():
        print(name)