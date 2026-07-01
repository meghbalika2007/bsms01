print("print left diagonal pattern matrix with alphabetsin asecending order:")
ascii=65
for i in range(6):
    for j in range(i+1):
        print(chr(ascii),end="")
        ascii+=1
    print()
