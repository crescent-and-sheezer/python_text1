# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/10 9:31
# @File: pizza.py
def make_pizza(size,*toppings):
    print("\nMaking a " +str(size)+
    "-inch pizza with the following topping:")
    for topping in toppings:
        print("- "+topping)