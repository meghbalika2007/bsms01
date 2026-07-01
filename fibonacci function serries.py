def  fibonacci(max):
    a=0
    b=1
    while a<=max:
        yield a
        a,b=b,a+b
def generatefibo(n):
    for i in fibonacci(n):
        print(i)
n= int(input("enter no."))
print("the fibonacci serries is : ",generatefibo(n))

