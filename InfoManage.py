# create an empty list to store students name
students_list = []
# craete an empty dictionary to store students details
students_dict = {}


# Prompting user to input name
name = input("Enter student name: ")
# Prompting user to input age
age = int(input("Enter student age: "))
# Prompting user to input grade
grade = int(input("Enter student grade: "))


#Appending student name to list
students_list.append(name)
# storing student information in a dictionary
# key: name, value: age and grade
students_dict[name] = {"age": age, "grade": grade}


#Display the success/confirmation message
print(f"Student {name} added successfully!")

# Displaying current stored data
print("Students list:", students_list)
print("Student details:", students_dict)

# searching for a student record
# get student name from user input
search_name = input("Enter the name of the student to search: ")

# verify whether student is present in the dictionary
if search_name in students_dict:
    print(f"Found: {search_name}, Age: {students_dict[search_name]['age']}, Grade: {students_dict[search_name]['grade']}")
else:
    print("Student not found.")


#Remove student data
remove_name = input("Enter the name of the student to remove: ")
#Verify if student exist before removing
if remove_name in students_dict:
    #remove element from list
    students_list.remove(remove_name)
    #remove data from dictionary
    del students_dict[remove_name]
    print(f"Student {remove_name} has been successfully removed!")
else:
    print("Student not found.")

# Finally displaying updated data
print("Updated Students:", students_list)
print("Updated Student Details:", students_dict)