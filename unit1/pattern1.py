#create a numeric right angled triangle pattern
# 1 2 3 4...


rows=int(input("Enter number of rows : "))
for i in range(1 + rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    print() #new line

# o/p
'''
Enter number of rows : 3

1 
1 2 
1 2 3 
1 2 3 4 
'''


