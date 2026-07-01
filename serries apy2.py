# 1,11,111,1111.......
n = int(input("Enter the number of terms :"))
s=0
for i in range(1,n+1):
    s= s*10+1
    print(s,end=",")
    
