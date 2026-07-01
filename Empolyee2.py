n=int(input("no.of employee : "))
l1=[]
for i in range(n):
    Employee=dict()
    name= input("Enter the name  :   ")
    sal= int(input("Enter the sal : "))
    d= input("Enter the  dapr :   ")
    l= input("enter location : ")
    Employee["name"]=name
    Employee["sal"]= sal
    Employee["dept"]=d
    Employee["loc"]=l
    l1.append(Employee)
#print(l1)
for j in range(len(l1)):
    if l1[j]['sal']>13500 and l1[j]['dept']== "acc":
        print(l1[j]['name'])
