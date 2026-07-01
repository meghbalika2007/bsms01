num = int(input("Enter a number:"))
l=9
h=0
while num>0:
    d = num%10
    
    if d > h:
        h=d
    if d < l:
        l=d
    num=num/10
print("highest number:",h)


