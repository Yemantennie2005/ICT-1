#Countdown Timer
num = 10
while num >= 1:
    print(num)
    num -= 1

print("Time's up!")

#Sum until zero
total = 0
while True:
    number = int(input("Enter integer number: "))
    if number == 0:
        break
    total += number
print("Total sum:", total)

#Create a program
correct_username = "admin"
correct_password = "1234"
attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Incorrect credentials. Attempts left:", attempts)
if attempts == 0:
    print("Account Locked")

