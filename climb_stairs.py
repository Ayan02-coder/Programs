#climbing stairs to reach at the top 
#there are n stairs. you can climb either 1 or 2 stairs at time . find the number of ways that a person can reach at top.

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
    
def coun(s):
    return fib(s + 1)
    
s = 10
print(coun(s))
