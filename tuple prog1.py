t=tuple()
n=6
i=1
a=0
b=0
while (i<=n):
    num=int(input("enter  elements :  "))
    t=t+(num,)
    i=i+1
print(t)
for i in range(0,len(t)):
    if t[i]%2==0:
      a=a+1
    else:
        b=b+1
print("odd item are :" , b)
print("even item are :" , a)
