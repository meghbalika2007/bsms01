def costprice(cost):
    if cost>200:
        return cost*0.8
    if cost<200:
        return cost*0.9
c= int(input("enter the cost: "))
print(costprice(c))
