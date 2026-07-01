def calculate(x,y):
    return x+y,x*y,x-y,x/y,x%y
n1=int(input("enter number 1:  "))
n2=int(input("Enter number 2:  "))
add,mum,sub,div,mod= calculate(n1,n2)
print("sum of the given numbers : " ,add)
print("sub of the given numbers : " ,sub)
print("product of the given numbers : " ,mum)
print("divition of the given numbers : " ,div)
print("remainder of the given numbers : " ,mod)

