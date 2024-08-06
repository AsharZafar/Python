def square_of_number():
    num=int(input("enter the number to be squared:\n"))
    square=num**2
    print(f"the square of the {num} is{square}")
square_of_number()


#                    PARAMETERS AND ARGUMENTS IN A FUNCTION
#                      the variables written in function definition are calld paramenter or
#                        the values supplied during a function call are called as arguments   
def salary_inc(name,eos,currentsalary):
    if eos>=1:
        if currentsalary <50000:
            incriment=currentsalary*.20
            newsalary=currentsalary+incriment

        elif currentsalary >=50000 and currentsalary <=100000:
            incriment=currentsalary*.50
            newsalary=currentsalary+incriment

        elif currentsalary >=100000 and currentsalary <=150000:
                incriment=currentsalary*.10
                newsalary=currentsalary+incriment
            
        else:
                incriment=currentsalary*.05
                newsalary=currentsalary+incriment
                print(f'''
            name of employe     :{name}
            year of servise     :{eos}
            current sallary     :{currentsalary}
            incriment           :{incriment}
            new salary          :{newsalary}
            ''')
    else:
        print("there is no incriment for you this year")
salary_inc("ashar", 2, 100000)

#                                  keyword arguments
#                                  salary_inc(name="ashar",eos= 2,currentsaalry= 100000)           





    



                                    #return function :it return values
                                    # 

def built_person(firstname,lastname,age=''):
    person={'first name':firstname,'last name':lastname}
    if age:
        person['age']=age
    return person
musician=built_person('ashar','zaf')
print(musician)



                                #\

def names(firstname,lastname):
    fullname=firstname+lastname
    return fullname.title()
while True:
    print("\n enter your namr \n or press q to exit")
    f_name=input("enter first name:\n")
    if f_name=="q":
        break
    else:
        l_name=input("enter your last name:\n")
    if l_name=="q":
        break
    full_name=names(f_name, l_name)
    print(f"hello{full_name}!")



                                        #

def make_album(artist,album_title,tracks=""):
    album_dicts={'artist':artist,'album':album_title}
    if tracks:
        album_dicts['tracks']=tracks
    return album_dicts
studio=[]
while True:
    artist=input("enter artist name or press q to exit:\n")
    if artist=="q":
        break
    album=input("enter album name or press q to exit:\n")
    if album=="q":
        break
    tracks =int(input("enter number of tracks or press q to exit:\n"))
    if tracks=="q":
        break
    studio.append(make_album(artist,album,tracks))
print(studio)



                                #

def my_sum(alist):
    total=sum(alist)
    return total
print(my_sum([1,2,3,4,5,6,7,8,9,10]))
