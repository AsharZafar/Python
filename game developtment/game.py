
import random


def gameWin(comp,user):
    if comp==user:
        return tie
    elif comp=="s":
        if user=="w":
            return False
        elif user=="g":
            return True
    elif comp=="w":
        if user=="g":
            return False
        elif user=="s":
                return True
    elif comp=="g":
        if user=="w":
            return True
        elif user=="s":
            return False


randno=random.randint(1, 3)

a= print("comp turn")
User=input("your turn input gun (g) ,water (w) , or snake(s):\n")
if randno==1:
    comp="g"
elif randno==2:
    comp="w"

else:
    comp="s"

a=gameWin(comp,User)

if a==None:
    print("tha game is a Tie")
elif a:
    print("you win")
else:
    print("you loose")

print(f"you choose {User}")
print(f"computer choose {comp}")

