# diff between for loop and while loop
a=0
while a<10:
    print("01_hello",a)
    a+=1



    #flag in while loop

    #user can choose the loop ending
flag=True
dishes=[]
while flag:
    dish=input("enter your favourite dishes here or 'q' to exit:\n")
    if dish=='q':
        flag=False
    else:
        dishes.append(dish)
print(dishes)


                            #tuples

                            #it is like a list but it is immutable

