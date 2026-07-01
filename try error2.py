import math
print ("code to test wrong type of arguments")
try:
    num1=int(input("Enter the first number: "))
    result1=math.sqrt(num1)
    print("sqrt: ",result1)
except ValueError:
    print("Please enter only positve numbers")
try:
    num2=int(input("Enter the second number"))
    result2=math.pow(num1,num2)
    print("Pow:",result2)
except ValueError:
    print("please enter only numbers")
finally:
    print("Test only types;wrong no.of requires requires*args")
