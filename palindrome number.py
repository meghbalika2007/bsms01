# palindrome number
n = int(input("Enter the number of terms :"))
t = n
rev = 0
while(t>0):
    d=t%10
    rev=rev*10+d
    t=t//10
if n==rev:
    print(n,"is palindrome number.")
else:
   print(n,"is NOT a palindrome number.") 
    
    
    
