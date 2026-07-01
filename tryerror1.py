a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
try:
    if b==0:
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("Please enter a non zero value for b")
    
            
