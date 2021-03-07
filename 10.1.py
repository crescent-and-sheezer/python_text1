# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/11 13:51
# @File: 10.1.py
'''
filename = 'pi_digits'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday,in the from mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the digits of pi!")
else:
    print("Your birthday does not appear in the digits of pi!")
'''
filename = 'pi_digits'
with open(filename) as file_object:
	lines=file_object.readlines()
for line in lines:
	line=line.replace('python','C')
	print(line.rstrip())