def myfunc( mylist ):
     print("\n\t Inside CALLED Function ")
     print("\t listed recevied: ",mylist)
     mylist[0]+=2
     print("\t list within call function after change : ", mylist)
     return
l1=[1,3,4]
print("list before call function: ", l1)
myfunc(l1)
print("\nlist after function call : ",l1)


     
