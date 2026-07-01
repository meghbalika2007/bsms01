Student=dict()
n =int(input("no, of students:  "))

for i in range (n):
    name= input("Enter student name:    ")
    print("Enter mark of physcis,chemistry and maths:")
    l=[]
    for j in range(3):
        m=eval(input("Enter marks :"))
        l.append(m)
    Student[name]=l
print("display students with marks above 90:")
for k,v in Student.items():
    c=0
    avg=0.0
    for a in v:
        c+=a
        avg=c/3
        if avg >90:
            print(k)

