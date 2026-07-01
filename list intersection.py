L1=[5,4,6,8,20]
L2=[2,5,67,20]
L=[]
for i in L1:
    if i in L2:
        L.append(i)
print("print the first list: ",L1)
print("print the second list: ",L2)
print(L)        
        
