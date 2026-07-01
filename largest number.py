#1
a= int (input("pls enteryour 1st no."))
b= int (input("pls enteryour 2nd no."))
c= int (input("pls enteryour 3rd no."))
max,min=0,0
if a>b and a>c:
    max=a
    if b>c:
        min=c
    else:
        min = b
elif b>a and b>c:
    max=b
    if a>c :
        min =c
    else:
        min=a
elif c>a and c>b:
    max = c
    if b>a :
        min =a
    else:
        min=b
else:
    print(" wrong input :")
print("Largest number :",max ,"Smallest :", min)
