def myfunc(mylist):
    print("\Inside CALLED Function now :")
    print("\t list recevied :",mylist)
    mylist.append(2)
    mylist.extend([5,1])
    print("\t List within called function , after changes : ",mylist)
    mylist.remove(5)
    print("\t List within called function , after changes : ",mylist)
    return
list1=[1]
print("list before function call :",list1)
myfunc(list1)
print("\list after function call : ",list1)
