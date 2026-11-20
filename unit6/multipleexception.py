# one block for multiple exception

try:
    num=int(input("enter number:"))
    result=100/num
    print("result is:", result)
except (ZeroDivisionError,ValueError):
    print("Invalid operation")