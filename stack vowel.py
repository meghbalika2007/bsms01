NoVowel=[]
Vowel="AEIOUaeiou"
def PushNV(N):
    for i in range(len(N)):
        voweltest=False
        for letter in N[i]:
            if letter in Vowel:
                voweltest=True
                break
            if voweltest==False :
                NoVowel.append(N[i])
                All=[]
                for i in range(5):
                    w=input("Enter a  word : ")
                    All.append(w)
                    PushNV(All)
                if len (NoVowel)==0:
                    print("Emptystack")
                while len(NoVowel)!=0:
                    print(NoVowel.pop(),"",end='')
                    print()
                    
                        
