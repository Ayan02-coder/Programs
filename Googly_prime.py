#check number is googly prime number
#googly prime = sum of digit in it is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
n = input("number:")
sum = 0
for i in n:
    sum += int(i)
    
a = is_prime(sum)

if a == True:
    print("Googly Prime")
else:
    print("NOT Googly Prime")
