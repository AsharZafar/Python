class Dog():
    def __init__(self,name,age,):


        ## attribute##
        self.name=name
        self.age =age

        #actions
    def sit(self):
      '''simulate a dog sitting in response to a command'''
      print(f"{self.name} is sitting")
    def roll_over(self):
        print(f"{self.name} is rolling over ")

dog1=Dog('tony', 2)
print(dog1.age)
print(dog1.name)

dog1.sit()
dog1.roll_over()

#######################

dog2=Dog('toby', 1)

print(dog1.age)
print(dog1.name)

dog1.sit()
dog1.roll_over()

############

dog3=Dog('terry', 123)
print(dog1.age)
print(dog1.name)

dog1.sit()
dog1.roll_over()
dog3=Dog('terry', 12)

##############################################################################

class patient():
    def __init__(self,name,gender,disease,contact_info):
      self.name=name
      self.gender=gender
      self.disease=disease
      self.contact_info=contact_info

    def name(self):
      print(f"{self.name}is name of patient")
    def disease(self):
      print(f"{self.name} has {self.disease} ")

    def contact_info(self):
      print(f"{self.name}'scontact info is {self.contact_info}")

     ######### GETTER

    def get_name(self):
       return self.name
    
    ######################  SETTER

    def set_name(self,new_name):
      self.name = new_name

patient1=patient('xyz', 'male', 'high bp', 123456)
print(patient1.name)

######################### UPDATING ATTRIBUTES #####################################
patient1.disease="low bp"
print(patient1.disease)
patient1.set_name('xyz')
print(patient1.name)




################### GETTERs $ SETTERS METHOD ################################

  #  def get_name(self):
   #    return self.name
    
   # ######################  SETTER

  #  def set_name(self,new_name):
  #    self.name = new_name


