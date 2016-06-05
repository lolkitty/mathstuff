n = True
l = False
f = input("Enter a number: ")
f = int(f)
p = int(input("Enter a number: "))
x = input
i = p
while n:
    l = False
    for x in range(f, p):
        if i % x == 0:
            pass
        else:
            l = True
            break
    if l == True:
        i = i + 1
    else:
        n = False
print(i)
input(" ")
