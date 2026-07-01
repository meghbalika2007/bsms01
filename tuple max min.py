t=tuple()
n=5
i=1
a=0
b=0
while (i<=n):
    num=int(input("enter  elements :  "))
    t=t+(num,)
    i=i+1
print(t)
max=t[0]
min=t[0]
for i in range(5):
    if t[i]>max:
       max= t[i]
    if t[i]<min:
        min =t[i]
print("Max is :",max)
print("Min is :",min)



