def Lshift(Arr,n):
    l=len(Arr)
    for x in range(0,n):
        y=Arr[0]
        for i in range(0,l-1):
            Arr[i]=Arr[i+1]
        Arr[l-1]=y
    print(Arr)
arr=[10,20,30,40,12,11]
print(Lshift(arr,2))
