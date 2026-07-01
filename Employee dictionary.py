#16
Employee=dict()
n=eval(input("Enter employee:"))
for i in range (n):
    name =input("Enter employee name : ")
    sal=eval(input("Every salaray : "))
    Employee[name]= sal
print("Display the dictionary : ", Employee)
L1=[]
L2=[]
for k,v in Employee.items():
    if v>57000:
        L1.append(k)
        L2.append(v*(15/100))
print("Display the employee details whose salary is more than 57000")
for i in range(len(L1)):
    print("Employee name :",L1[i],"Pf: ",L2[i])
