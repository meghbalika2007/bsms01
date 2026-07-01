w=int (input("Enter the weight "))
if w<= 500 :
    charge =100
else :
    w = w -500

    if w % 50 == 0:
        charge = 100 + (w // 50)  * 80
    else :
        charge = 100 + (w // 50 + 1) * 80 

print ("charge=" , charge)
