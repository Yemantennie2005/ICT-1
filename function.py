def sum():
    a = 5
    b = 10
    print("The sum of a and b is:", a + b)

def product():
    a = 5
    b = 10
    print("the product of a and b is:", a * b)

sum()#calling the sum function.
product()#calling the product function.

def sum_with_parameters (x, y):
    print("The sum of", x, "and", y, "is:", x + y)
sum_with_parameters(3, 7)
def product_with_parameters(x, y):
    print("The product of", x, "and", y, " is:", x * y)
product_with_parameters(3, 7)

def sum_with_return(x, y):
    return x + y
print("The sum of 4 and 6 is:", sum_with_return(4, 6))

def product_with_return(x, y):
    return x * y
print("The product of 4 and 6 is:", product_with_return(4, 6))

#excercise
m1 = float(input("Enter mark1: "))
m2 = float(input("Enter mark2: "))
m3 = float(input("Enter mark3: "))

def calculate_total(m1, m2, m3):
    return m1 + m2 + m3
print("The total marks is:", calculate_total(m1, m2, m3))

def calculate_average(total):
    return total / 3
print("The average mark is:", calculate_average(m1 + m2 + m3 / 3))
average = (m1 + m2 + m3) / 3
if average >= 50:
    print("Pass")
else:
    print("Fail")

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("\nEnter a number to check even or odd: "))
print("Number is:", check_even_odd(num))
