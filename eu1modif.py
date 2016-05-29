#Finds all the multiples of x and y, below n.
x  = int(input("Enter a number: "))
y  = int(input("Enter a number: "))
n  = int(input("Enter a number: "))

num = list(range(0,n))
num.append(n)
#for i in range(0,len(num)):
#  if num[i]%x != 0:
#    del num[i]
#  elif num[i]%y != 0:
#   del num[i]
i = 0
while i < len(num):
  if num[i]%x != 0:
    del num[i]
  elif num[i]%y != 0:
    del num[i]
  else:
    i = i + 1
print(num)
