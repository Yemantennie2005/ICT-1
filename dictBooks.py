BookDetails = dict({"Python Programming": "John smith", "Python Fundamentals": "Alice Johnson", "Python Interview Questions": "Jane Doe"})
for keys in BookDetails:
    print(keys, BookDetails [keys])

#loop inside a loop
for i in range(1,4):
    for j in range(i):
        print(f"Outer Loop Interation{i}, inner loop iteration {j+i}")
for i in range(1,4):
    for j in range(i):
        print(f"Outer Loop iteration {1}, inner loop iteration j+i")
for i in range(4):
    for j in range(i):
        print("*", end = "")
    print()

for i in range (1,6):
    for j in range(1, i+1):
        print(j, end = "")
    print()
for i in range (6,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()
for i in range (5,0,-1):
    for j in range(i):
        print("*", end = "")
    print()