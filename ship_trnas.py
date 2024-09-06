@ # A ship needs to trnasport people from one point to another . if ship has capacity of  c and there are n people.
  #task is return numbers round 
#c is capacity
#n is no of passanger
c,n = map(int,input().split())
sum = int(n/c)
if n % c != 0:
    sum += 1
print(sum)
