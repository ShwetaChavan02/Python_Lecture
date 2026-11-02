def greet_person(name):
    print("Hello, " + name + "!")
def change_case(text):
    result = ""
    for ch in text:
        if ch.isupper(): # convert uppercase to lowercase
            result += ch.lower()
        elif ch.islower(): # convert lowercase to uppercase
            result += ch.upper()
        else: # for non-alphabetic characters, keep them unchanged, symbols, numbers, etc.
            result += ch
    return result