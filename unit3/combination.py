#combination of *args and **kwargs

def display(*args, **kwargs):
    print(args)
    print(kwargs)

display(10, 20, 30, name="Shweta", age=22)