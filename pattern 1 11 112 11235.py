n=5
for i in range (1,n+1):
    a=1
    b=0
    c=0
    for j in range (i):
        c=a+b
        print(c,end="")
        a=b
        b=c
    print() 
