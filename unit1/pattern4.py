# alphabetic pattern 
# row wise right angled triangle pattern
'''
A
B B 
C C C 
D D D D
'''

for i in range (5):
    for j in range (i+1):
        print(chr(65+i), end=" ")
    print()