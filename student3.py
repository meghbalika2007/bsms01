fileout=open("D:\\student.txt","w")
for i in range(5):
    name=input("enter name of student: ")
    fileout.write(name)
    fileout.write("\n")
fileout.close()
    
