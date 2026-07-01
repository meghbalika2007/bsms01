def myfunc(mylist):
    print("\Inside CALLED Function now")
    print("\t list recevied :",mylist)
    new=[2,4]
    mylist.append(6)
    print("\t list within called function , after changes: ", mylist)
    return
list1=[1,3,6]
print("List before function call :",list1)
myfunc(list1)
print("\n after the function call: ", list1)
