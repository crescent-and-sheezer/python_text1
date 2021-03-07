# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/28 10:57
# @File: 8.2.1.py
'''
def make_shirt(shirt_size,shirt_type):
    print("\nThe shirt size is "+shirt_size+".")
    print("The shirt type is "+shirt_type.title()+".")
make_shirt('M','Hello!')
'''
'''
def make_shirt(shirt_size,shirt_type="I love Python."):
    print("\nThe shirt size is " + shirt_size + ".")
    print("The shirt type is " + shirt_type.title() + ".")
make_shirt(shirt_size='M')
make_shirt(shirt_size='L')
'''
def describe_city(city_name,country_name="Iceland"):
    print(city_name.title()+" is in "+country_name.title()+".")
describe_city('reykjavik')
describe_city('bbbccccc')
describe_city(city_name='shanghai',country_name='china')