print("serries of x**1,x**2,x**3......")
x= int(input("Enter an integer: "))
n= int(input("No.of terms of serries :"))
sum =0
for i in range(n+1):
    print(pow(x,i),end="")
    sum = sum +pow(x,i)
print("/n sum of serries : " ,sum)
