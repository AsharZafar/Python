#-object oriented programning

               # attributes
     
class car():
    make="civic"
    model="2022"
    reg="2022"
    color="black"
    engine="1300cc"

  #             methods
def run():
    print("car is running")
def stop():
    print("car has been stopped")
def door_open():
    print("door opens")
def door_closes():
    print("door closes")





class human():
    def __init__(self,name,gender,age,blood_group):
     
        '''this function int is called as initializer
        .(constructor) values required in initializer are mendatory
        to supply to creat an object'''
                   ##############  ATTRIBUTES OF HUMAN ################### 
        self.name=name
        self.gender=gender
        self.age=age
        self.blood_group=blood_group

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def reaad(self):
        print(f"{self.name} is reading")


################################ now making object##########################################

human1=human("Ashar", 'MALE', '20','A+')
print(human1.name)
print(human1.gender)
print(human1.age)
print(human1.blood_group)

print(human1.eat())
print(human1.sleep())
print(human1.reaad())


########### creating another object of human ########################
human2=human("saad", "MALE", 17, "a+")

print(human2.name)
print(human2.gender)
print(human2.age)
print(human2.blood_group)

print(human2.eat())
print(human2.sleep())
print(human2.reaad())

