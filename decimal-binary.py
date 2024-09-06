#print decimal to binary

n = int(input("number: "))
l =[]

while n > 0:
    l.append(n%2)
    n //= 2

l.reverse()
a =  ''.join(map(str, l))
print(a)

# sum of binary 

n = int(input("number: "))
sum = 0
while n > 0:
    sum += n % 2
    n //= 2
    
print(sum)
    
