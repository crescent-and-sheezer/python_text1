# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/22 21:09
# @File: 5.3.py

'''
user_names=['admin','Eric','Bill','Lance','Kirito']
for user_name in user_names:
    if user_name=='admin':
        print("Hello admin,would you like to see status report?")
    else:
        print("Hello "+user_name.title()+",thank you for logging in again")
'''
'''
user_names=[]
if user_names:
    for user_name in user_names:
        if user_name=='admin':
            print("Hello admin,would you like to see status report?")
        else:
            print("Hello "+user_name.title()+",thank you for logging in again")
else:
    print("We need to find some users!")
'''
'''
current_users=['Admin','Eric','Bill','Lance','Kirito']
new_users=['John','vally','kirito','bill','ken']
for new_user in new_users:
    if new_user.title() in current_users:
        print("You need other name.")
    else:
        print("Your username can pass.")
'''
list=[1,2,3,4,5,6,7,8,9]
for value in list:
    if value==1:
        print(str(value)+"st")
    elif value==2:
        print(str(value)+"nd")
    elif value==3:
        print(str(value)+"rd")
    else:
        print(str(value)+"th")