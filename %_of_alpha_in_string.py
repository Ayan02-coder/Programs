# football  o having percentage of 25% in it

def findper(str,n):
    b = 0
    for i in str:
        if i == n:
            b += 1
        else:
            continue
    c = (b/len(str)) * 100
    print(int(c),"%",sep="")
str,n = input().split()
findper(str,n)
