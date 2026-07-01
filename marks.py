c=int(input(" how many students: "))
f=open("D://marks.txt","w")
for i in range (c):
    print("the details of students",(i+1), "below:   ")
    rollno=int(input("the rollno. "))
    name=input("name")
    marks=float(input("grades are:   "))
    record=str(rollno)+","+name+","+str(marks)
    f.write(record)
    f.write("\n")
f.close()


