a=input("enter your name")
if (a==saad):
    print("welcome ssd")
else:
    print("nikal")


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