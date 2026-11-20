#else block

try:
    num=int(input("enter number:"))
    result=100/num
except ZeroDivisionError:
    print("division by zero is not allowed")    
else:
    print("result is:", result)