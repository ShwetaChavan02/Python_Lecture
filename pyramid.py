# numeric pyramid

n=5 
sp=5 
#spaces
for i in range(1, n + 1):
    for s in range(0, sp):
        print(end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")

    print()
    sp -= 1

# o/p
'''
     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5
'''