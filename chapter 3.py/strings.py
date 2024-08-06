name='ashar'
greetings ='goodmorning '
c=greetings + name
print(c) 

                               #congatinating
enter ='zafar mehmood'
print(enter [0])  # isme ye hai keh z=0  a=1 f=2 a=3 r=4  square bracket use hota hai specify krne k liye
print(enter [1])  # isme ye hai keh z=0  a=1 f=2 a=3 r=4  square bracket use hota hai specify krne k liye
print(enter [2])  # isme ye hai keh z=0  a=1 f=2 a=3 r=4  square bracket use hota hai specify krne k liye
print(enter [3])  # isme ye hai keh z=0  a=1 f=2 a=3 r=4  square bracket use hota hai specify krne k liye
print(enter [4])  # isme ye hai keh z=0  a=1 f=2 a=3 r=4  square bracket use hota hai specify krne k liye

# matrices
print(enter [0:5])
print(enter [:5])

#spacing
print(enter [0:13:2])                   #2 is spacing #0 to 13 


                           #string functions (COMMANDS)


print(len(enter))                       #length of the string

print(enter.endswith("mehmood"))        #ends with btata hai matlab mehmood pe khatam horha hai

print(enter.count('a'))                 #counts number of elements specified
print(enter .find('zafar'))
print(enter.replace('zafar','ashar'))   #replaces character 
print(enter.capitalize())               #capitilize first character
print(enter.find("meh"))                #finds the specified string
print(enter.isdigit())                  #
email=" asharzafar25@gmail.com"
print(email.strip())                    #removes spaces from left and right similarly rstrip()
                                        # removes left gap and similarly lstrip() removes left gap

                          
                                     
                            #list strings
                        #     for more use python docs

l1=[1,56,3,9,7,5,5]
 

l1.sort()                               #re arranges according to ascending order
          
print(l1)                      

l1.reverse()                           #reverse the list a/c to descending order
print(l1)

l1.append(25)                               #adds 25 to end of the list  
print(l1)

l1.pop(2)
print(l1)                   #removes 3rd index from the list

l1.remove(9)               #removes 9 from the given list
print(l1) 


                        #escape sequence characters

                              #\n   (breaks line)   \t (spacing )

ash= "ashar\nzafar \t mehood"
print(ash)                             


                          #problems
                          #Q1
naam = input('enter your name \n')
print("goodmorning and welcome ,"+naam)


                         #  Q2
                         # letter 

letter = '''Dear <|name|> you are, selected as
the manager of this company. 
Date<|date|>'''

name =input('enter named:')
date = input('enter dated:')
letter=letter.replace ("<|name|>", name)
letter=letter.replace("<|date|>" ,date)
print(letter)


                              #Q3
                              # double spaces

st="ashar is a good boy he is a mechanical  engineer"
doublespaces= st.find("  ")
print(doublespaces)


                                     #Q4
                              
st=st.replace("  ", ",")
print(st)                             









                             # end=" "       (ends the line)                      