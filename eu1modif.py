#Finds all the multiples of x and y, below n.
x  = input("Enter a number: ")
y  = input("Enter a number: ")
n  = input("Enter a number: ")

num = range(0,n)
num.append(i)
for i in range(0,len(num)):
  if num[i]%x != 0:
    del num[i]
  elif num[i]%y != 0:
    del num[i]
print(num)
