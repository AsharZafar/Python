'pillars of object oriented programing'


#inheritance
#polymorphism
#encapsulation
#abstraction

class person():
    def __int__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def walk(self):
        print(f'{self.name} is walkng')


class student(person):
    pass

s1=student("asd",20,"male")
print(s1.name)

class athlete(person):
    pass
a1=athlete()
print(a1.walk('asd'))
