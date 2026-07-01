n=int(input(" enter your number : "))
mum=1
sum=0
while n>0:
    n%10
    n = n/10
    mum = mum *n
    sum = sum +n
if sum == mum :
    print (" Spy no.")
else:
    print("Not spy no .")
