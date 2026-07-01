n=int(input("Enter how many sublist to store:"))
Value=[]

for i in range(n):
    val=[]
    m=int(input("How many no.s to be added(max5) : "))
    print("Sublist:  ", i+1)
    for j in range(m):
        a= int(input("Enter value: "))
        val.append(a)
    Value.append(val)
print("Nested list : ",Value)
for i in range (len(Value)):
    max_n=Value[i][0]
    min_n=Value[i][0]
    for j in range(len(Value[i])):
        if Value [i][j]> max_n:
             max_n= Value [i][j]
        if Value [i][j]> min_n:
             min_n= Value [i][j]
    print("Sublist:  ", i+1)
    print("Max No : ",max_n)
    print("Min No: ",min_n)
