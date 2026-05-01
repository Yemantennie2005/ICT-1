def print_pattern(n):
    # when n reaches 1, we simply print star and stop recursion 
    if n == 1:
        print("*")
        return
    #First, go deeper into recursion 
    print_pattern(n - 1)

     # print stars on return (increasing order)
     # This ensures the pattern builds upwards (1 → n)

    print("* " * n)

# input size of pattern
n = int(input("Enter a number: "))
# start recursion
print_pattern(n)