# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/22 13:46
# @File: 4.3.py

'''
my_foods=['pizza','falafel','carrot cake','tomato','meat']
print("The first three items in the list are:")
print(my_foods[:3])
print("Three items from the middle of the list are:")
print(my_foods[1:4])
print("The last three items in the list are:")
print(my_foods[-3:])
'''
'''
my_pizzas=['a','b','c','d','e']
friend_pizzas=my_pizzas[:]
friend_pizzas.append('f')
print("My favorite pizzas are:")
print(my_pizzas)
print("My friend's favorite pizzas are:")
print(friend_pizzas)
'''
my_foods=['pizza','falafel','carrot cake','tomato','meat']
friend_foods=my_foods[:]
friend_foods.append('noole')
for my_food in my_foods:
    print(my_food)
for friend_food in friend_foods:
    print(friend_food)