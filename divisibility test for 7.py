c=0
l=[]
t=()
d={}
for i in range (200,300):
    if i%7==0 and i%5 !=0:
        c+=1
        l.append(i)
        t=t+(i,)
        d[i]=i**0
print(l)
print(t)
print(d)
