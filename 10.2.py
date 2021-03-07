# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/11 15:08
# @File: 10.2.1.py
'''
filename = 'guest'
with open(filename,'w') as file_object:
    name = input("Please write your name:")
    file_object.write(name)
    print("\nWelcome to here!")
filename0 = 'guest_book'
with open(filename0,'a') as file_object:
    file_object.write("1")
'''
filename = 'why'
with open(filename,'a') as file_object:
    while True:
        reason = input("Please tell us,why do you like computer:\n")
        if reason == 'quit':
            break
        else:
            file_object.write(reason+"\n")