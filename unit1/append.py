# write a content in the file
# append
# when we write the file the content is added at the last of the file

f = open("sample.txt", "a")

f.write("This is appended text from Shweta.")

f.close()

print("Content appended successfully")