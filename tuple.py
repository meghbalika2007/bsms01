# tuple
t=tuple()
n=10
c1=0
c2=0
i=0
while(i<=n):
    num=int(input("Enter the numbers:"))
    t=t+(num,)
    i+=1
for a in t:
    if(a%2==0):
        c1+=1
    else:
         c2+=1
print("no.f even :",c1)
print("no.f odd :",c2)
