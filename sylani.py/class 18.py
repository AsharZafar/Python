#e → a constant with a value that is an approximation of Euler's number (e)
#exp(x) → finding the value of ex;
#log(x) → the natural logarithm of x
#log(x, b) → the logarithm of x to base b
#log10(x) → the decimal logarithm of x (more precise than log(x, 10))
#log2(x) → the binary logarithm of x (more precise than log(x, 2))
#Note: the pow() function:

#pow(x, y) → finding the value of xy (mind the domains)



from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))



#ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
#floor(x) → the floor of x (the largest integer less than or equal to x)
#trunc(x) → the value of x truncated to an integer (be careful - 
# it's not an equivalent either of ceil or floor)
#factorial(x) → returns x! (x has to be an integral and not a negative)


from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))



from random import random

for i in range(5):
    print(random())







from random import randrange, randint



print(randrange(1), end=' ')     #The first three invocations will generate an integer taken 
print(randrange(0, 1), end=' ')   # (pseudorandomly) from the range (respectively):
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))


     #The previous functions have one important disadvantage -
     #  they may produce repeating values even if the number of subsequent
     #  invocations is not greater than the width of the specified range.
    
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')


                  #
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

from platform import machine

print(machine())


from platform import processor

print(processor())


from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))


# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))



    # Demonstrating the chr() function.

print(chr(97))
print(chr(945))




alpha = "abdefg"

print(alpha[1:3])          
print(alpha[3:])      
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])      


#          output
#bd
#efg
#abd
#e
#e
#adf
#beg




#The in operator shouldn't
#  surprise you when applied to strings - 
# it simply checks if its left argument (a string)
#  can be found anywhere within the right argument 
# (another string)



# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))



print("aAbByYzZaA".index("A"))


# Demonstrating the list() function:
print(list("abcabc"))

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))


###############################
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

##############################################

#isalnum() checks if the string contains only digits or alphabetical characters
#  (letters),
#  and returns True or False according to the result.
# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())


############################

#The isalpha() method is more specialized - it's interested in letters only.


# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())

###############################################
#The lower() method makes a copy of a source string,
#  replaces all upper-case letters with their lower-case counterparts,
#  and returns the string as the result. Again, the source string remains untouched


# Demonstrating the lower() method:
print("SiGmA=60".lower())


#####################################

#rstrip method 
print("cisco.com".rstrip(".com"))
print("ashar".rstrip("ar"))               #removes from back            


# Demonstrating the split() method:
print("phi       chi\npsi".split())



#The startswith() method is a mirror reflection of endswith() - 
# it checks if a given string starts with the specified substring.
# Demonstrating the startswith() method:

print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")




############################################




#The swapcase() method makes a new string by swapping the case of 
# all letters within the source string:
#  lower-case characters become upper-case, and vice versa.


# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

print()

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())

print()

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())

                ##
                #
                #

