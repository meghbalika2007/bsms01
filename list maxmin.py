n=int(input ("Enter the the no.of elements:"))
List1=[]
for i in range(n):
    a=int(input("Enter:"))
    List1.append(a)         
max=List1[0]
min=List1[0]
for i in range(n):
    if List1[i]>max:
       max= List1[i]
    if List1[i]<min:
        min =List1[i]
print("Max is :",max)
print("Min is :",min)
