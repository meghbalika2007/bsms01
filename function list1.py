def EOreplace(L):
    for i in range(len(L)):
        if L[i]%2==0:
            L[i]+=1
        else:
            L[i]-=1
    return L
a=[10,20,36,45,12,90,1,3,93]
print(EOreplace(a))
