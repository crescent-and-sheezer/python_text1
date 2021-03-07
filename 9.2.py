# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/10 15:30
# @File: 9.2.1.py
'''
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
        self.served=0
    def describe_restaurant(self):
        print("The restaurant's name is "+self.name.title()+"."
              "And the restaurant's cuisine type is "+self.type.title()+".")
    def open_restaurant(self):
        print("The restaurant is opening.")
    def number_served(self):
        print(str(self.served))
    def set_number_served(self,number):
        if number >= 10:
            print("You can't!")
        elif number <10 and number >=0:
            self.served = number
            print("welcome to 'T&F'.")
    def increment_number_served(self,num):
        self.served += num

my_restaurant=Restaurant('T&F','赣菜')
print("My restaurant's name is " + my_restaurant.name.title() + ".")
print("My restaurant's cuisine type is " + my_restaurant.type.title() + ".")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served()
my_restaurant.set_number_served(5)
my_restaurant.number_served()
my_restaurant.increment_number_served(100)
my_restaurant.number_served()
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

first_user=User('花泽','香菜')
first_user.describe_user()
first_user.greet_user()
first_user.login_attempts()
first_user.increment_login_attempts()
first_user.login_attempts()
first_user.reset_login_attempts()
first_user.login_attempts()