n= int (input("Pls enter the number of terms :"))
a = 1
b = 0

for i in range (n):
    c = a+b *2
    print (c, end =" ")
    a=b
    b=c
