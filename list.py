 
# number of elements as input
n = int(input("Enter number of elements : "))
 lst =list()
# iterating till the range
for i in range(0, n):
    ele = eval(input())
    # adding the element
    lst.append(ele) 
 
print("the elements are : ",lst)
