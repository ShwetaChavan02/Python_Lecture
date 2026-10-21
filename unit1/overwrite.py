# over writing the file
# while using the W mode the content is overwrited

f = open("sample.txt", "w")

f.write("This is new content from Shweta.")

f.close()

print("File content overwritten successfully")