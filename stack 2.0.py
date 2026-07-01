Stackitem=[]
def push(sitem):
    c=0
    for k in sitem:
        if(sitem[k]>=75 ):
            Stackitem.insert(-1,k)
            c=c+1
    print("The count of element in stack is :",c)
ditem={"Pen":106,"Pencil":59,"Notebook":80,"Eraser":25}
push(ditem)
print(Stackitem)
