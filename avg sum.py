def calsum(a,b,c):
    s=a+b+c
    return s
def average (x,z,y):
    sm= calsum(x,y,z)
    return sm/3
n1=int(input("enter n1: "))
n2=int(input("enter n2: "))
n3=int(input("enter n3: "))
a=average(n1,n2,n3)
print("tne average is: ",a)
