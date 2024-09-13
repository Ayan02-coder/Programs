a =['d','a','a','c','c','b','a','d']
b = {}
for i in range(len(a)):
    if a[i] not in b:
        b[a[i]] = 1
    else:
        b[a[i]] += 1
for i in b:
    print(f"{i} occurs {b[i]} times")
