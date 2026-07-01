s=[]
def Push(items):
    count=0
    for k in items:
        if(items[k]>700):
            s.append(k)
            count+=1
    print("The count of  elements in stack is :",count)
items=dict()
n=int(input("Enter no.of items: "))
for i in  range(n):
    key=input("Enter items:  ")
    value=eval(input("Enter prices: "))
    items[key]=value
print(items)
Push(items)
print(s)

