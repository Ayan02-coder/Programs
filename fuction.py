#function

#define function
def sum(a,b):  $#parameter
    #c = a+b
    #return c
    return a + b  #return output
    
print(sum(5,4))
print(sum(553,425))#calling of function wth argument


#calculat avg of 3 number
def avg(a,b,c):
    return (a+b+c) / 3
print(avg(1,2,3))
print(avg(3,3,3))
print(avg(98,97,95))

#default paramater

def cal_prod(a,b=2):
    print(a * b)
    return a * b
    
cal_prod(1)
cal_prod(9,3)
