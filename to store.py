def create():
    f=open("D:\\poem.txt","wt",)
    for i in range(5):
        s=input("Enter a line :")
        f.write(s)
        f.write('\n')
    f.close()
create()
