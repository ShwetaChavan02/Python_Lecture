# Count word frequency in names (handle duplicates) 
# and store results in a dictionary {name: count}.

f = open("file.txt", "r")
names = f.read().splitlines()
f.close()

count = {}

for name in names:
    count[name] = count.get(name, 0) + 1

print(count)