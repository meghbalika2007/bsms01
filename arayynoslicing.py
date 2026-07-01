# initializing list 
test = [1, 4, 5, 6, 7, 8, 9, 12]
 
# printing the original list
print ("The original list is : " , str(test))
 
# using insert() + pop()
# shift last element to first
test.insert(0, test.pop())
 
# printing result
print ("The list after shift is : " , str(test))
