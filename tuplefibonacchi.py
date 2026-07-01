a=0
b=1
print(a,",",b,end=" ,")
for i in range(2,9):
    next=a+b
    print(next,end=" ,")
    a=b
    b=next
    print(tuple(next ))
