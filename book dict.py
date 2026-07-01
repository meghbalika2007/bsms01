l1=['Ruskin Bond','karnetkar','Lipus','Tagore']
l2=[[700,'1-107-2005'],[1250,'17-11-2005'],[1780,'10-03-2007'],[500,'01-02-1899']]
book={}
for i in range(len(l1)):
    book [l1[i]]=l2[i]
print("The og dictinary: ", book)
for k,v in book.items():
    if v[0]>780:
        print(k,"the price of the book is:","release date:",v[0])
