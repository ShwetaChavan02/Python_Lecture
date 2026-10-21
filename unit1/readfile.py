# file operations
#read file

f = open("txtfile1.txt")
print(f.read())
f.close()

#when  not using WITH statement we need to close the file after reading it
