p = int (input("pls enter the principle : "))## Principal (1+Rate/100)n - Principal
r= int (input("pls enter the rate of interest : "))
t = int(input("pls enter the time period : "))
si = p*r*t/100.0
ci = (p*(1+r/100.0)**t)-p
print("the simple interest is :" ,si)
print("the compound interest is : " ,ci)
