   #              modules /libraries/

import math

print(12//5)
print(12/5)
print(math.ceil(2.7))           #returns very next integer


print(math.floor(2.7))            #returns very last integer

import module_to_call                #importing the module to the file

module_to_call.square_of_number()



#                            exceptions
# 
#                  also called as errors

#valid syntax: an integer can divide  another integer
#12/2 , 3/2
#but 0 cannot be divide 

try:
   a=int(input("enter a number to be divided :"))
   b=int(input("enter a number to  divide :"))
   res=a/b
   print(res)
#except ZeroDivisionError:
#   print("you cannot divide a number by zero")
#except ValueError:
#   print("insaan ka bacah banja warna ghar aa maarunga")       


      #itne saare laganay ke bjaye hai ek hi lagado
except Exception as e:
   print(f"there was an exception caugt successfully\n {e}")



from math import pi as PI, sin as sine

print(sine(PI/2))