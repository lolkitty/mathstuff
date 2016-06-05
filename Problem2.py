n = [1, 1, 2]
i = 2
f = True
l = 0
h = int(input("Give me a number: "))
while f:
    if n[i-1] + n[i] > h:
        break
    l=n[i] + n[i-1]
    n.append(l)
    i=i + 1
print(n)
result = 0
for i in range(0,len(n)):
    if n[i]%2==0:
        result = result + n[i]
print(result)
input(" ")
