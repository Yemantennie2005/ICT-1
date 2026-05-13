# Create a dummy excel file named Students.xlsx in write mood
file = open('Students.xlsx', 'w')

# Write column heading
file.write("Name, ID\n")

# Store at least 5 students' names and IDs  
file.write("Samten,   0279\n")
file.write("Yangchen, 0265\n")
file.write("Adamz,    0276\n")
file.write("Dendup,   0256\n")
file.write("Kuenzang, 0278\n")

# Close the file after writing
file.close()

#Open the same file in read mode
file = open('Students.xlsx', 'r')

students = file.read() # Read all contents from the file

print(students) # Display the content of the file

file.close() # Close the file after reading

# Ask user to enter a name to search
searchN = input("Enter a name to search: ")
found = False #Variable to check whether the name exists
with open('Students.xlsx', 'r') as file:
    for student in file:
        if searchN.lower() in student.lower(): # Compare input names wihtout case sensitivity
            print(student) 
            found = True # Mark as found
            break # Stop searching once found

# If name is not found, show message
if not found:
    print("Name not found in the file.")
print()