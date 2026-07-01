#11
n= int(input("Enter how manystrings to added in a list:"))
wl=list()
for a in range(n):
    s= input("Enter a word : ")
    wl.append(s)
print("original list of strings : ",wl)
wl2=[]
for word in wl:
    wl2.append(word[::-1])
print("list of reverse stringn: ",wl2)
