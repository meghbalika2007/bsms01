# fionacchi serries
n = int(input("pls enter the no.of terms : "))
a = 1
b = 0
c = 0
for i in range(n):
    c= a+b
    a=b
    b=c
print(c, end = " ")

