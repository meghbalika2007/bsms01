import math
a=float(input("Pls enter the 1st coiefficient:"))
b=float(input("Pls enter the 2nd coiefficient:"))
c=float(input("Pls enter the 3rd coiefficient:"))
D = b**2 - (4 * a * c)
print (D)
if D>=0:
  x = (-b + math.sqrt(D))/(2*a)
  y = (-b - math.sqrt(D))/(2*a)
  print (math.sqrt(D))
  print ("the  two  value is x is : ",x,y)
else:
    print ("Invalid discriminent : ", D)
    
