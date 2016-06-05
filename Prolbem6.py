a = int(input("GIVE ME A NUMBER: "))
squares = [x**2 for x in range(1,a+1)]
cats = range(1,a+1)
s = sum(cats)**2
t = sum(squares)
print(s-t)
input(" ")
