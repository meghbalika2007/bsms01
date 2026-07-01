row =5
for i in  range (0,row):
    print(" "*i ,end=" ")
    a=1
    for j in range(row-i,0,-1):
        print(a,end=" ")
        a=a+1
    print()    
 
