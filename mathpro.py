#2
import math
a= int (input("pls enter your coeffiecient(a) = "))
b= int (input("pls enter your coeffiecient(b) = "))
c= int (input("pls enter your coeffiecient(c) = "))
d=(b**2-(4*a*c))
if d>0:
    print("two real roots:")
    r1=(-b+ math.pow(d,0.5))/(2*a)
    r2=(-b- math.pow(d,0.5))/(2*a)
    print("root1 :",r1)
    print("root2 :",r2)
elif d==0:
    print("1 egual roots equal:")
    r1=r2=-b/(2*a)
    print(r1)
else:
    print("Imaginary roots:")
    
