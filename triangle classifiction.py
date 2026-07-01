# classify a triangle as obtuse or acute or rightangled triangle
a = int (input ("enter your first angle "))
b = int (input ("enter your second angle"))
c = 180 -(a+b)

if a<90 and b<90 and c<90:
    print("  it is acute angle tringle ! ")
elif a==90 or b==90 or c==90 :
    print (" Right angled tringle ! ")
else:
    print(" obtuse angled triangle ! ")
