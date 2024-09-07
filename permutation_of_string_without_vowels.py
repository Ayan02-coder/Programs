# permutation of string without vowels 

def fact(num):
    if num == 0 or num == 1:
        return 1
    return num * fact(num - 1)

str = "hello my name is Ayan"
list = []
for i in str:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == " ":
        continue
    else:
        list.append(i)
        
print(fact(len(list)))
