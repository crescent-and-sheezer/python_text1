# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/22 17:56
# @File: 5.2.1.py
'''
alien_color=['green','yellow','red']
if 'green' in alien_color:
    print("Your score is five.")
else:
    print()
'''
'''
alien_color=['green','yellow','red']
alien_color='green'
if alien_color=='green':
    print("You have five points")
alien_color = 'red'
if alien_color == 'green':
    print("5 points get！")
else:
    print()
'''
'''
alien_color=['green','yellow','red']
alien_color='yellow'
if alien_color=='green':
    print("You have 5 points")
else:
    print("You have 10 points")
'''
'''
alien_color=['green','yellow','red']
alien_color='red'
if alien_color=='green':
    print("You have 5 points")
elif alien_color=='yellow':
    print("You have 10 points")
else:
    print("You have 15 points")
'''
'''
age=54
if age<2:
    print("baby")
elif age>=2 and age<4:
    print("child")
elif age>=4 and age<13:
    print("young teenager")
elif age>=13 and age<20:
    print("teenager")
elif age>=20 and age<65:
    print("man")
else:
    print("old man")
'''
favorite_fruits=['apple','bananas','orange']
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'orange' in favorite_fruits:
    print("You really like orange!")