arr = [9,55,2,20,54,55,55,3]
arr.sort(reverse = True)
for i in range(len(arr)):
    if arr[i] != arr[i+1]:
        print(arr[i+1])
        break
    else:
        continue
        
