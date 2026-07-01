def MakePush(Package):
    a=int(input("Enter package tittle:"))
    package.append(a)
    return print(Package)
def Makepop(Package):
    if(Package==[]):
        print("Stack empty")
    else:
        print("Delete element:",Package.pop())
        
