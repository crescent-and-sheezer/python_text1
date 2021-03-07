# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/29 12:34
# @File: 8.4.py

'''
names=['小艾','小龙','小乔','小侠']
def show_magicians(names):
    for name in names:
        print(name)
show_magicians(names)
'''
'''
names=['小艾','小龙','小乔','小侠']
names1=[]
def show_magicians(names):
    for name in names:
        print(name)
def make_great(names):
    while names:
        now_name=names.pop()
        print("the Great"+now_name)
        names1.append(now_name)
show_magicians(names)
make_great(names)
'''
names=['小艾','小龙','小乔','小侠']
names1=[]
def show_magicians(names):
    for name in names:
        print(name)
def make_great(names):
    while names:
        now_name=names.pop()
        print("the Great"+now_name)
        names1.append(now_name)
show_magicians(names[:])
make_great(names)
