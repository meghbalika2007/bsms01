row = 5
for i in range(0,row):
    print(" "*i,end=" ")
    a=0
    for j in range(row-i,0,-1):
        a=a+1
        print(a,end= " ")
    print()
