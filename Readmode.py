greetings = open("hello.txt", "r")
print(greetings)
greetings.close()

#file properties
f = open("hello.txt", "r")
print("filename: ", f.name)
print("file mode: ", f.mode)
print("Is the file closed?: ", f.closed) #False
f.close() #closing file
print("Is the file closed? : ", f.closed) #True

#Reading a file
f = open("hello.txt", "r")
contents = f.read()
print(contents)
f.close

#Writing a file
newFile = open ("newFile.txt", "w")
#print the objects of the file created
print(newFile)
newFile.write("this is a new file created by python")
newFile.close() #file closed
FileOverwrite = open("newfile.txt", "w")
FileOverwrite.write("The contents of the newFile is now changed.")
FileOverwrite.close()

#Appending a file
appendFile = open("hello.txt", "a")
appendFile.write("\n\nDon't forget to smile today!")
appendFile.close()

#with statement
with open ("hello.txt", "r") as f:
    contents = f.read()
    print(contents)