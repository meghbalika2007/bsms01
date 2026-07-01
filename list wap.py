list1=[]
n=int(input("No.of elements:"))
for i in range (n):
    item = int(input("Enter the value:"))
    list1.append(item)
check= int(input("Enter the data:"))
c=0
for i in range (n):
    if check==list1[i]:
        c=c+1
print("frequency=",c)
