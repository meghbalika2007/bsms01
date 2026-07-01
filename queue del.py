def insertQ(Names):
    Names=input("Enter Name to be inserted: ")
    List.append(Names)
def DeleteQ(Names):
    if (Names==[]):
        print("Queue empty")
    else:
        print("Delete Value is :",Names[0])
del(Names[0])
