# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/9 11:18
# @File: 8.5.py

'''
def sandwich(*shicais):
    print("\nMaking a sandwich with the following toppings:")
    for shicai in shicais:
        print("- "+shicai)
sandwich('meat')
sandwich('milk','meat')
sandwich('milk','egg','meat')
'''
'''
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('wu','xufan',location='poyang',hobby='music',field='computer')
print(user_profile)
'''
def make_Car(name,model,**messages):
    Car = {}
    Car['name'] = name
    Car['model'] = model
    for key,value in messages.items():
        Car[key] = value
    return Car
car = make_Car('subaru','outback',color='blue',tow_package=True)
print(car)