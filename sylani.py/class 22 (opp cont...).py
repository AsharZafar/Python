class Car():

 #"""A simple attempt to represent a car."""#######################################

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


##############################  MODIFYING ATTRIBUTES ###############################

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
############################# INCRIMENTING ################################ 
    def increment_odometer(self, miles):
        self.odometer_reading += miles


    def fill_gas_tank(self):
        print("gas is being filled ")


my_new_car = Car('audi', 'a4', 2016)


car2=Car('ford', 'sabre', 1970)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

car2.update_odometer(23)
car2.read_odometer()

print(car2.get_descriptive_name())
car2.read_odometer()



###################################  UPDATE     #########################################

car3 = Car('subaru', 'outback', 2013)
print(car3.get_descriptive_name())

car3.update_odometer(23500)
car3.read_odometer()
       ################################ INCRIMENT      ############################
car3.increment_odometer(100)
car3.read_odometer()


#######################################################################################

class ElectricCar(Car):
    def __init__(self, make, model, year):

        super().__init__(make, model, year)             # super(). means parent class
        self.battery_size = 70

    def describe_battery(self):

        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print("electric car doesnto have a gaskit OR fuelkit it runs on fuel")




e1=ElectricCar('honda','civic', 2022)
e1.describe_battery()

e1.fill_gas_tank()






####################################################################

###################   OVER RIDING METHOD OF PARENT CLASS #####################

def ElectricCar(Car):
    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


############################ Instances as Attributes #######################

class Battery():
    def __int__(self,manufacturer,waranty,output,cells):
        self.manufacturer=manufacturer
        self.waranty=waranty
        self.output=output
        self.cells=cells
    def charge(self):
        print("Battery is charging")

    def description(self):
        print(f'''
                 BATTERY DETAILS
                 ===============
                 MANUFACTURER:{self.manufacturer}
                 WARANTY     :{self.waranty}
                 OUTPUT      :{self.output}
                 CELLS       :{self.cells}
            ''')


class ElectricCar(Car):
    def __init__(self, make, model, year):

        super().__init__(make, model, year)             # super(). means parent class
        
        self.Battery= Battery('osaka',3,27,31)


    def describe_battery(self):

        print("This car has a " + str(self.battery_size) + "-kWh battery.")

e4=ElectricCar('kawasaki', 'latest', 2020)

e4.battery.description()



 def __iter__(self):

     is