staff_list=["ashar","saad","bla"]
for staff in staff_list:
    print(f"you are walcomed to be hired  {staff}")
                 
                 
                 
                 #RANGE FUNCTION
for a in range(5):
    print(a,end="")

for a in range(1,25):
    print(a,end="")

for b in range(1,25,3):
    print(b,end="")


#        for loop keywords

#                         continue    (skips the letter)

#                          break        (stops)



#                           if

for num in range(1,11):
    print(num)
    if num==7:
        break

                   #

evens=[]
odds=[]

for a in range(5):
        num=int(input("enter the number here:\n"))
        if num%2==0:
            print(f"the given number{num} is even")
            evens.append(num)
        else:   
            print(f"the given number{num} is odd")
            odds.append(num)

print(evens)
print(odds)


                                            #.split functiom



evens=[]
odds=[]
numbers=input("enter your favourite number to seperate  with , ").split(',')


for num in numbers:
        
        if int(num)%2==0:
            evens.append(num)
        else:   
            odds.append(num)

print(f"evens{evens}")
print(f"ods{odds}")




                        #

