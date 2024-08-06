#                                       WHILE LOOPS

#        THERE ARE TWO TYPES OF LOOPS
#            while loop and for loop


i=0
while i<10:
    print("yes"+str(i))
    i=i+1
print("done")

                                                #quiz

i=0
while i<5:
    print("ashar")
    i=i+1


fruits=["banana","mangoes","strawberry","grapes"]
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1


                            # FOR LOOP

fruit=["banana","mangoes","strawberry","grapes"]
for item in fruit:
    print(fruit)

                                #RANGE FUNCTION

for i in range(8):               #   8 will not be included
    print(i)
for i in range(1,8):               #   will start from 1
    print(i)
for i in range(2,8):               #   will start fronm 2 
    print(i)

                                         #  FOR WITH ELSE
for i in range(10):               #   will start fronm 2    
    print(i)
    if i==5:
        break                   #   WILL CONTINUE TILL 5 AND WILL NOT GO TO ELSE COMMAND
else:
    print("this is the end")    #   not used because if command in executed

for i in range(10):               #   will skip 5 in the counting   
    if i==5:
        continue    
    print(i)

                               #PASS STATEMENT
i=10                              
if i>0:
    pass                            #it is is a null statement doesnot do anytng prevents from error
print("ashar")

