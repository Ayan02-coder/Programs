arr = [9,55,2,20,54,55,55,3]
arr.sort(reverse = True)
for i in range(len(arr)):
    if arr[i] != arr[i+1]:
        print(arr[i+1])
        break
    else:
        continue



#2nd approch   
arr = [9,7,75,67,87,87]

u = list(set(arr))  # Remove duplicates

if len(u) == 1:
    if len(u) > 1:
        print(u[1])
    else:
        print("no")# The second largest unique element
else:
    if len(u) > 1:
        print(u[-2])  # The second largest unique element
        
