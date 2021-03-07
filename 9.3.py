# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/10 16:48
# @File: 9.3.py

'''
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
    def describe_restaurant(self):
        print("The restaurant's name is "+self.name.title()+"."
              "And the restaurant's cuisine type is "+self.type.title()+".")
    def open_restaurant(self):
        print("The restaurant is opening.")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['apple','banana','strawberry','berry']
    def show_ice(self):
        for flavor in self.flavors:
            print(flavor)
My_ice=IceCreamStand('T&F','icecream')
My_ice.open_restaurant()
My_ice.describe_restaurant()
My_ice.show_ice()
'''
'''
class User():
    def __init__(self,first_name,last_name):
        self.first = first_name
        self.last = last_name
        self.login_attempt = 0
    def describe_user(self):
        print("The user'fullname is "+self.first.title()+self.last.title()+".")
    def greet_user(self):
        print(self.first.title()+self.last.title()+" welcome to here.")
    def login_attempts(self):
        print(self.login_attempt)
    def increment_login_attempts(self):
        self.login_attempt = self.login_attempt + 1
    def reset_login_attempts(self):
        self.login_attempt = 0
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        for key in self.privileges:
            print(key)
Admin1=Admin('wu','xufan')
Admin1.show_privileges()
'''
'''
class User():
    def __init__(self,first_name,last_name):
        self.first = first_name
        self.last = last_name
        self.login_attempt = 0
    def describe_user(self):
        print("The user'fullname is "+self.first.title()+self.last.title()+".")
    def greet_user(self):
        print(self.first.title()+self.last.title()+" welcome to here.")
    def login_attempts(self):
        print(self.login_attempt)
    def increment_login_attempts(self):
        self.login_attempt = self.login_attempt + 1
    def reset_login_attempts(self):
        self.login_attempt = 0
class privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        for key in self.privileges:
            print(key)
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privilege = privileges()

Admin1=Admin('wu','xufan')
Admin1.privilege.show_privileges()
'''
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class Battary():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_size(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        else:
            print()

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battary()
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_size()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_size()
my_tesla.battery.get_range()