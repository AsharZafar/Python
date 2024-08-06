x=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
largest_number=max(x, b,c)
print("the largest number is",largest_number)




x=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
largest_number=min(x, b,c)
print("the least number is",largest_number)


while True:
    word = input("You're stuck in an infinite loop!\nEnter the secret word to leave the loop: ")
    if word == "chupacabra":
        break
print("You've successfully left the loop!")
