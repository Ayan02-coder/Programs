#find occurrence of element b in string a

a = str(input())
b = str(input())
c = 0
for i in a:
    if i == b:
        c += 1
print(c)
