
print("QUESTION 1\n multiplication table")
num=int(input("enter the number:\n"))
for i in range (1,11):
   # print(str(num)+"X"+str(i)+"="+str(i*num))              
    print(f"{num}X{i}={num*i}")                   #DOES THE SAME THING F STRING MAKES IT EASY


print("QUESTION 2")

l1=["ASHAR","SAAD","ZAFAR","JAVARIA"]
for naam in l1 :
    if naam.startswith("S"):
        print("HELLO" + naam)
    else:
        print("kaise ho yrrrr")

#Q3
l=input("enter number")
while num<11:
    print(str(l))





print("QUESTION 3")                     
                            #
num=int(input("enter the number :\n"))
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
if prime:
    print("this number is prime")
else:
    print("this number is not a prime number")


                              #QUESTION (5)
print("QUESTION 5")

num=int(input("enter the number here:\n"))
factorial=1
for i in range(1, num+1):
    factorial = factorial * i
print(f"THE FACTORIAL OF {num} IS {factorial}")




                                 #QUESTION 6

print("QUESTION 6")

n=4
for i in range(4):
    print("*"*(i+1))

print("QUESTION 7")
num=3
for i in range(3):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))

