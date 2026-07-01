stackItem=[]
def Push(SItem):
    count=0
    for k in SItem:
        if(SItem[k]>=75):
            stackItem.append(k)
            count=count+1
      print("The count of elements in the\stack is :",count)
Ditem={"Pen":106,"Pencil":59,"Notebook":80,"Eraser":25}
Push(Ditem)
print(stackItem)
