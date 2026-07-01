n= int(input("Enter how many elements to store : "))
L=list()
print("input number for list  : ")
for i in range(n):
    a=int(input("Enter:"))
    L.append(a)
print("Modified list :",L)
print("original list:",L)
for j in range(0,len(L)-1,2):
    L[j],L[j+1]=L[j+1],L[j]
print("Modiefied list :",L)
    
