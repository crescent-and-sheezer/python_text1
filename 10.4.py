# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/11 17:55
# @File: 10.4.py
'''
import json
fav_num=input("Enter your favorite number: ")
file_name="favnum.json"
with open(file_name,'w') as f:
	json.dump(fav_num,f)
with open(file_name) as f:
	num=json.load(f)
	print("I know your favorite number! It's "+num+".")
'''
'''
import json
def get_favnum():
    file_name = "favnum.json"
    try:
        with open(file_name) as f:
            num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return num
def print_favnum():
    num = get_favnum()
    if num:
        print("I know your favorite number! It's " + num + ".")
    else:
        file_name = "favnum.json"
        num = input("Enter your favorite number: ")
        with open(file_name, 'w') as f:
            json.dump(num, f)
print_favnum()
'''
import json
def get_sorted_user():
    '''获取存储的用户名'''
    file_name = "username.json"
    try:
        with open(file_name) as f:
            user_name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user_name
def get_new_user():
    '''获取新的用户名'''
    user_name = input("Enter your name: ")
    file_name = "username.json"
    with open(file_name, 'w') as f:
        json.dump(user_name, f)
    return user_name
def greet():
    '''问候用户并指出名字'''
    user = get_sorted_user()
    if user:
        print("Welcome " + user + "~")
        ask = input("Am I right? Enter 'y' or 'n': ")
        if ask == 'y':
            pass
        elif ask == 'n':
            user = get_new_user()
            print("Welcome " + user + "~")
    else:
        user = get_new_user()
        print("Welcome " + user + "~")
greet()