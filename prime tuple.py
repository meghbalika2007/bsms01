t1=(2,23,14,17,34,45,29,90 )
print(t1)
c=0
flag = 1
for i in t1:
    if t1(i)!=1:
      for a in range(2,t1(i)):
          if t1(i)%a==0:
              c=c+1
      if c==2:
          flag=2
      else:
         flag=3
for i in t1:
    if flag==2:
        t1(i),t1(i+1)=t1(i+1),t1(i)
        
    print("THe modified tuple is: " , t1)       
        
          
    
    
