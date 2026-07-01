st=input("Enter a sentence: ")
st=st.split()
c=0
for word in st:
    if word[0]in"Pp":
        print(word,end=" ")
        c=c+1
print("Number of words starting with P/p:  ",c)
