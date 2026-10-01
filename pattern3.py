# alphabetic pattern 
'''
A
A B 
A B C 
A B C D
'''
#code 2
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()

'''
# code 1 
for i in range (1, 6):
    for j in range (1, i):
        print(chr(64+j), end=" ")
    print()
'''