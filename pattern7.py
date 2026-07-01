#7
row,a=4,1
for i in range(1,row+1):
    for k in range(1,row+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(a,end=" ")
        a=a+1
    print()
    
