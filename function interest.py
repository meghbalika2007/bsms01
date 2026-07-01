def interest(p,r=0.10,t=2):
    a=p*r*t
    return a
prin=float(input("enter principle amt: "))
print("the simple interest of the compound is : ")
si1=interest(prin)
print("Rs.",si1)
roi= float(input("enter rate of : "))
time=int (input("enter time : "))
si2=interest(prin,roi/100,time)
print("the simple interest of the compound is(si2) : ",si2)

