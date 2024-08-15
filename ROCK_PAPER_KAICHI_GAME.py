import random
def game(you,comp):
    if you=='s':
        if comp=='s':
            print("Draw")
            return False
        elif comp=='p':
            return False
        else:
            return True
    elif you=='p':
        if comp=='p':
            print("Draw")
            return False
        elif comp=='k':
            return False
        else:
            return True
    elif you=='k':
        if comp=='k':
            print("Draw")
            return False
        elif comp=='s':
            return False
        else:
            return True
    else:
        print("INVALID CHOICE")
        return False
    
w=l=0
n=int(input("Enter number of times you wish to play at once: \n"))
print("PLEASE ENTER ALL CHOICES IN LOWERCASE LETTERS OR IT WILL BE CONSIDERED INVALID CHOICE AND YOU WILL LOSE AUTOMATICALLY ")
print("----GAME OF STONE PAPER KAICHI STARTS----")
while n>0:  
    y= input("Your turn : Stone(s), Paper(p), Kaichi(k)  \n")
    print("Computer's turn : Stone(s), Paper(p), Kaichi(k) ")
    rand=random.randint(1,3)
    if rand==1:
      c='s'
    elif rand==2:
      c='p'
    else:
      c='k'
    print (f"Computer chose: {c}")
    results=game(y,c)
    if results:
      print ("WIN")
      w+=1
    else:
      print ("YOU LOSER !!!")   
      l+=1
    n-=1
    print(f"Number of turns remaining : n")

if w>l:
    print("LUCk SHINES ON YOU TODAY!!!WASSUP GRAND WINNER  *WINK*")
else:
    print("YOU FOOLISH IDIOT *ROFL*!!! THOUGHT YOU COULD WIN WITH ME? WASSUM GRAND GRAND GRANDEST LOSER???")
    print(f"P.S - you won {w} time(s)")
