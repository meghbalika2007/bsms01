str=input("Enter a word : ")
l=len(str)
first= str[0]
last=str[l-1]
tempstr=""


for i in range(0,l):
    if i==0:
        tempstr+=last
    elif i==l-1:    
        tempstr+=str[0]
    else:
        tempstr+=str[i]


print("The modified word is : ",tempstr)
