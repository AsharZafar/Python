mydict={
    "ashar":"s/o zafar mehmood \nGENDER: MALE   \n STUDIES : NED UNIVERSITY  \nlocation adress : flat no. G2 sahmim  ",
    "saad":"s/o zafar mehmood  \n GENDER: MALE \n STUDIES : FORMEN COLLEGE  \nlocation adress : flat no. G2 sahmim ",
    "javaria":"d/o zafar mehmood \n GENDER: FEMALE \n STUDIES : FEDERAL SECONDARY SCHOOL  \nlocation adress : flat no. G2 sahmim ",
    "kosar":"w/o zafar mehmood \n GENDER: FEMALE \n STUDIES : KARACHI UNIVERSITY  \nlocation adress : flat no. G2 sahmim ",
    "location adress":"flat no. G2 sahmim"
}
print("OPTIONS ARE",mydict.keys())
a=input("enter family members name:\n " )

print("INFORMATION :" ,mydict.get(a) )
