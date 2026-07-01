# Amstrong number
n = int(input("Enter a number:"))
order = len(str(n))
t=n
s = 0
while(t>0):
    d=t%10
    s = s +(d**order)
    t=t//10
if n==s:    
    print(n,"is an amstrong number.")
else:
   print(n,"is NOT a amstrong number.") 
    
    
