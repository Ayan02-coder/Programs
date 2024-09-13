# find pernumation of con , if vowel are on fixed position


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)
    
a ="abbccdee"
for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u": #if i in "aeiou"
        a = a.replace(i,"")

b ={}
for i in range(len(a)):
    if a[i] not in b:
        b[a[i]] = 1
    else:
        b[a[i]] += 1
c= 1
for i in b:
    c *= fact(b[i])
    
d = fact(len(a))
e = d/c
print(int(e))
