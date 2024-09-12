def differenceofSum(n. m)

The function accepts two integers n, m as arguments Find the sum of all numbers in range from 1 to m(both inclusive) that are not divisible by n. Return difference between sum of integers not divisible by n with sum of numbers divisible by n.
def diff(n,m):
    sum = 0
    sum1 = 0
    for i in range(1, m+1):
        if i % n == 0:
            sum += i
        else:
            sum1 += i
    return abs(sum - sum1)

n = int(input())
m = int(input())
print(diff(n,m))
