n = int (input("Enter no.of nested tuple:"))
l1=[]
l2=[]
player=()
for i in range(n):
    pn = input("Emter name:")
    avg = eval (input("Enter avg score : "))
    cen= int (input("Enter no .of centuries :"))
    l1.append(tuple([pn,avg,cen]))
player= tuple(l1)
for a in player:
    if (a[i]>45)and(a[i]>30):
        print(a for a in player)
        
print("Records of player centuries :")
