#              set is a collection of non repetative elements


a={1,2,3,4,1,2}              #1,2 will not be repeated

print(type(a))                           #class=set

# importannt: this sntax will show an empty dictionary

b={}
print(type(b))                  #<class 'dict'>

#this syntax will show an empty set

c=set()
print(type(c))               # <class 'set'>

c.add(4)                     #adding elements to the set

c.add(5)
c.add(5)
c.add(5)
print(c)

#c.add([1,2,3,4])               #cannot add list and dictionary to the set
c.add((1,2,3,4))               #can add tuple to the set
print(c)

                                     # Q1

mydict={
    "ashar":"s/o zafar mehmood \nGENDER: MALE   \n STUDIES : NED UNIVERSITY  \nlocation adress : flat no. G2 sahmim  ",
    "saad":"s/o zafar mehmood  \n GENDER: MALE \n STUDIES : FORMEN COLLEGE  \nlocation adress : flat no. G2 sahmim ",
    "javaria":"d/o zafar mehmood \n GENDER: FEMALE \n STUDIES : FEDERAL SECONDARY SCHOOL  \nlocation adress : flat no. G2 sahmim ",
    "kosar":"w/o zafar mehmood \n GENDER: FEMALE \n STUDIES : KARACHI UNIVERSITY  \nlocation adress : flat no. G2 sahmim ",
    "location adress":"flat no. G2 sahmim"
}
print("OPTIONS ARE",mydict.keys())
a=input("enter family members name:\n " )

print("INFORMATION :" ,mydict.get(a) )           # now it will not show an error

                                  #Q7

favlang ={}
a=input("enter your favourite language ashar : ")
b=input("enter your favourite language saad: ")
c=input("enter your favourite language javaria: ")
d=input("enter your favourite language abcde : ")
favlang["ashar"] =a
favlang["saad"] =b
favlang["javaria"] =c
favlang["abcde"] =d
print(favlang)

