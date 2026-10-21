# alphabetic pattern 
'''
A
B C 
D E F
G H I J
'''
#code 2
n=int(input("Enter the number of rows: "))
num=0
for i in range(n):
    for j in range(i):
        print(chr(65+num), end=" ") 
# ascii value of A, 
# as we have to print all alphanbets in sequence 
# so we are using num variable to increment the ascii value of A
        num += 1
    print()
