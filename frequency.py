def MakeInventory(s):
    freq={}
    for i in s:
        freq[i]=freq.get(i,0)+1
        print(i,freq[i])
    return freq
string=input("Enter a string : ")
list1=string.split()
print(MakeInventory(list1))
