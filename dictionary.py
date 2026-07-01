ph=dict()
i=1
n=int(input("no.of date:"))
while i<=n:
    a=input("Name")
    b=input("phno")
    ph[a]=b
    i=i+1
x=input("Enter name to search:")
k=ph.keys()
for  a in k:
    if a==x:
        print(x,"phone no.",ph[i])
        break
else:
    print(x,"does not exist:")
