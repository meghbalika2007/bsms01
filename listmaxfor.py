def max_num(l):
    max=l[0]
    for i in l:
        if i>max:
            max =i
    return max
l=list()
n=int(input("enter no."))
for i in range (n):
    g=int(input("enter number : "))
    l.append(g)
print("the given list: ",l)
print("maximum value is : ",max_num(l))
