p = eval(input("Enter principle:"))
r = eval(input("Enter rate:"))
n= eval(input("Enter n:"))
CI= (p*(1+(r/100))**n)-p
print(CI)
A = CI+p
print("Total amt is :",A)
