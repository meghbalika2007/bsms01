n= int(input("Enter how many numbers to add : "))
val=list()
for i in range(n):
    a=int(input("Enter value :"))
    val.append(a)
print(val)
i=0
n=len(val)-1
while i< n:
    if val[i]%7==0:
        val[i],val[i+1]=val[i+1],val[i]
        i+=2
    else:
        i+=1
print(val)
    
