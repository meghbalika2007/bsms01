student=dict()
n=eval(input("Enter no.of students :"))
for i in range (n):
    name =input("Enter student name : ")
    print("Enter phy, chem,math,marks")
    l=[]
    for j in range(3):
        m=eval(input("Enter marks : "))
        l.append(m)
    student[name]=l
print("Student marks more than 90:")

for k,v in student.items():
        c=0
        avg=0.0
        for a in v:
            c+=a
        avg=c/3
        if avg>90:
            print(k)
