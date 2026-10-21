#cube sum of n natural numbers

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i ** 3

print("Sum of cubes =", sum)