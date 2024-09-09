#WAF to print all hashes in str before str and return all str

#a = "Ayan#sayyad#student#"
# Method 1
def hash(a):
    b = a.count("#")
    c = a.replace("#","")
    print("#"*b + c)
    
hash("Ayan#sayyad#student#uh")

# Method 2
def hash1(a):
    b = []
    c = []
    d = list(a)
    for i in d:
        if i == "#":
            b.append(i)
        else:
            c.append(i)
    print("".join(b+c))
    
hash1("Ayan#sayyad#student#uh")
