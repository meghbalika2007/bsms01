L1=['ruskin bond','Karnet Kar','Lipsus','Tagore']
L2=[[700,'10-07-2005'],[1250,'12-01-2007',],[1780,'10-03-2005'],[500,'01-02-1899']]
Book={}
for i  in range(len(L1)):
    Book[L1[i]]=L2[i]
print("The original dictionary :",Book)
for k,v in Book.items():
    if v[0]>780 :
        print(k,"-Book record-price, release date :",v[0])
