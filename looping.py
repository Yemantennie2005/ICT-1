name = input("Enter your name: ")
for i in name: 
    print(i)
li = ["Python Programming", "Pyhton Fundamentals", "Python Interview Questions"]
for x in li:
    print (x)
lenli = len(li)
for x in range(lenli) :
    print(li[x])

new_tuple = tuple(li)
for x in li:
    print(x)
lennew_tuple = len(li)
for x in range(lennew_tuple):
    print(new_tuple[x])
new_set =set(li)
for x in li:
    print(x)
