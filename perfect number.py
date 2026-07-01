n = int(input("Pls enter your number"))
count=0
sum=0
for i in range (1,n):
    if n%i==0:
        sum =sum+i
if sum == n :
    Print(n,"It is a perfect number")
else:
    print(n,"Itis not a perfect number")
