L1=[2,3,4,5,6,6,7,8,7,9,9]
L2=[]
L3=[]
for i in L1:
  if i not in L1:  
    x=L1.count(i)
    if x>1:
        L2.append(i)
    else:
        L3.append(i)
print(L2,L3)
