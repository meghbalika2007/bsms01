#1,12,123,1234.....
n = int(input("Enter the number of terms : "))
s=0
for i in range(1,n+1):
    s=s*10+i
    print(s,end=",")
    

