# keyword arguments

def my_function(animal, name):
    print("i have a ", animal)
    print("my",animal+"'s name is", name)
my_function(name="lucky",animal="cat")
# sequence doesnt matter as values are called using keywords
my_function(animal="cat", name="lucky")