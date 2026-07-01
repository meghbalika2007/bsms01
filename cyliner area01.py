# A cylinder
r = int (input("enter radius  : "))
h = int (input("enter height  : "))
csa = 2*22/7*r*h
tsa = 2*22/7*r*(h+r)
vol = 22/7 * r**2*h

print("the curved surface area of cylinder is : " , csa)
print("the Total surface area of cylinder is : " , tsa)
print("the volume of cylinder is : " , vol)
