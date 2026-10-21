#file opeartions
#read file with WITH statement

with open("txtfile1.txt") as f:
    print(f.read()) 
    #print(f.read(6)) this will print only first 6 characters
    ct = f.read()
    wt = ct.split()
    print("Total words:", len(wt))
    print("Total characters:", len(ct))
    
#while using WITH statement we don't need to close the file