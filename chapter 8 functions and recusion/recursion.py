                      # recursion in one which calls itself

#factorials 
n=3
product=1
for i in range(n):
    product=product * (i+1)
print(product)


                  #practice question

def smallest(num1, num2, num3):
    if (num1<num2):
        if (num1<num3):
            return num1
        else:
            return num3
    else:
        if(num2<num3):
            return num2
        else:
            return num3

m=smallest(12,55,2)
print("THE smallest HIGHEST NUMBER IS "+str(m))

#                                         practice question

                       

def maximum(num1, num2, num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m=maximum(12,55,2)
print("THE maximum HIGHEST NUMBER IS "+str(m))
    

                      #
    
def farenheit(cel):
    return(cel - 32)*(5/9)

c=int (input("enter the temperature in farenheigth: \n"))
f= farenheit(c)
print("the temperature in celsius is ="+str(f))


n=6
for i in range (n):
    print("*" * (n-i) )



                            #strip function

