name = input("Enter your name: ")
greet = lambda x: print ("Hello", x)
greet (name)

#Condition checking
even_odd = lambda x: "Even" if x % 2 == 0 else "odd"
num = int(input("Enter a number: "))
print(even_odd(num))

#Return multiple results
arith = lambda x, y: (x + y, x - y, x * y, x / y)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(arith (num1, num2))

#filter function
mylist = [1, 2, 3, 4, 5, 6]
even = filter (lambda x: x % 2 == 0, mylist)
print(list(even))

#map function
mylist = [1, 2, 3, 4]
double = map(lambda x: x * 2, mylist)
print(list(double))

#convert result of double to mylist
mynewlist = (list(double))
double = map(lambda x: x/2, mynewlist)
print(list(mynewlist))

#reduce function
from functools import reduce
mylist = [1, 2, 3, 4]
mul = reduce (lambda x, y: x * y, mylist)
print(mul)

#Student Excercise 
#positive/negative/zero
positive_negative_zero = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "zero"
num = int(input("Enter your number: "))
print(positive_negative_zero(num))
