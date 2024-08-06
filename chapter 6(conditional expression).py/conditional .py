#ifelse and if are multi way decisions taken by the program due to certain conditions in our code
# spaces after if statement are called as (indentation)(a tab or four spaces)

a=int(input("enter the number \n"))
if(a>3):
    print("the value is greater than 25")
elif(a>20):
    print("the valuse is geater than 25")

                # QUIZ

age=int(input("Enter youre age here:\n"))                #Integer should be used int() 
if(age>25):                                  
    print("yes")                                         # if greater than 
else:
    print("no")                                          # iff less than

# and or not operators 

b=int(input("enter the age  \n"))
if(b>18 and b<50):
    print("you  work with us")
elif(b>50):
    print("not allowed")
else:
    print("get lost")


                                             #practice set

                                       #Q!

num1 =int(input("enter number 1:"))                  
num2 =int(input("enter number 2:"))                  
num3 =int(input("enter number 3:"))                  
num4 =int(input("enter number 4:"))                  
if(num1>num4):
    f1=num1
else:
    f1=num4
if(num2>num3):
    f2=num2
else:
    f2=num3
if(f1>f2):
    print(str(f1)+"is the greatest")
else:
    print(str(f2)+"is the greatest")


                            #Q2
                        
sub1=int(input("enter fist subject marks\n:"))
sub2=int(input("enter second subject marks\n:"))
sub3=int(input("enter third subject marks\n:"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you have not even cleard the exam ")
elif(sub1+sub2+sub3)/3 <50:
    print("cleared the subject but havent cleared precentage criteria ")
else:
    print("nice keep it up :}")


                             #Q3
text=input("enter the comment here :\n")
if("make alot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click and earn money" in text):
    spam=True
    if(sapm):
        print("this text is a spam")
else:
    print("this is not a spam")


                        #Q4

name=input("enter your name:\n")
names=["ashar","saad","javaira","kosar","zafar"]
if name in names:
    print("family member")
else:
    print("you are not a family member")


                            #Q6
num=int(input("enter your name :\n"))
if num>90:
    grade= A1
elif num>80:
    grade= A
elif num>70:
    grade= B
elif num>60:
    grade= C
elif num>=50:
    grade= C
else:
    grade=failed
print("your result is :\n" + grade)


