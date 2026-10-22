# Read a file containing student names (one per line) and store them in a list.

file = open("file.txt", "r")

students = file.read().splitlines()

print(students)

file.close()