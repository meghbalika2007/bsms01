def Push(vehicle):
    for k in vehicle:
        if vehicle[k].upper()=="TATA":
            stack.insert(-1,k)
stack=[]
vehicle={"santro":"Hyundai","Nexon":"TATA","Safari":"Tata"}
Push(vehicle)
print(stack)
