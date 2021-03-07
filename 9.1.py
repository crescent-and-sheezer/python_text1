# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/10 10:57
# @File: 9.1.py

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

my_restaurant=Restaurant('T&F','赣菜')
print("My restaurant's name is " + my_restaurant.name.title() + ".")
print("My restaurant's cuisine type is " + my_restaurant.type.title() + ".")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
'''
# 第二题同第一题意义不大，忽略
class User():
    def __init__(self,first_name,last_name):
        self.first = first_name
        self.last = last_name
    def describe_user(self):
        print("The user'fullname is "+self.first.title()+self.last.title()+".")
    def greet_user(self):
        print(self.first.title()+self.last.title()+" welcome to here.")
first_user=User('花泽','香菜')
first_user.describe_user()
first_user.greet_user()