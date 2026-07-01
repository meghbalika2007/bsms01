print("The following pattern is: ")

a=65
for i in range(6):
    for j in range(i+1):
      print(chr(a),end="") 
      a=a+1
    print() 
