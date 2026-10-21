# position only argument

def my_function(name, /):
    print("HELLO", name)
my_function("shweta")
# it will never accept values in keywords forat
def student(name, age, /):
    print(name, age)

student("Shweta", 22)