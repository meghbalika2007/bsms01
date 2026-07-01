def create (arr):
    l2=[]
    print("original list:",l)
    for a in arr:
        if a%2==0:
            s=str(a)
            l2.append(int(s[::-1]))
    #a=17
        else:
            s=0
            while a!=0:
                s=s+a%10
                a=a//10
                l2.append(s)
    return l2
l=[17,18,27,38,47]
l=create(l)
print("Modified list :",l)
