#create a numeric reversed  right angled triangle pattern
# 4 3 2 1 0...

rows=int(input("Enter number of rows : "))
for i in range(rows, 0, - 1):
    for j in range(i, 0, -1):
        print(j, end=" ")

    print() #new line

# o/p
'''
Enter number of rows : 5
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
'''