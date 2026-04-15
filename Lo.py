for i in range(1,4): #outer loop iterates from 1 to 3
    for j in range(i):#inner loop iterate from 0 to i-1
        print(f"Outer loop iteration {i}, inner loop iteration {j+1}")

for i in range(4):
    for j in range(i):
        print("*", end = " ")
    print()

for i in range (1,6):
    for j in range(1, i+1):
        print(j, end ="")
    print()

for i in range(6,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()