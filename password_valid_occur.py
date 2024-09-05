n = int(input())
b = list(map(int,input().split()))

# if len(b) != n:
#     print("Enter correct number of elements")
# else:
ans = { }
for i in b:
  if i in ans:
    ans[i] += 1
  else:
    ans[i] = 1

occur = {}
for count in ans.values():
        if count in occur:
            occur[count] += 1
        else:
            occur[count] = 1
            
is_valid = True
for i in occur.values():
    if i > 1:
        is_valid = False
        break

if is_valid:
    print("valid")
else:
    print("not valid")
