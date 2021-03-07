# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/11 16:05
# @File: 10.3.py
'''
try:
    number1 = int(input("Please write number:"))
    number2 = int(input("Please write number:"))
except ValueError:
    print("请输入数字！")
print(number1 + number2)
'''
'''
while True:
    try:
        number1 = int(input("Please write number:"))
        if number1 == 'q':
            break
        number2 = int(input("Please write number:"))
        if number2 == 'q':
            break
    except ValueError:
        pass
    else:
        print(number1 + number2)
'''
'''
try:
    filename ='cats'
    with open(filename) as file_object:
        catname = file_object.readlines()
        print(catname)
    filename = 'dogs'
    with open(filename) as file_object:
        dogname = file_object.readlines()
        print(dogname)
except FileNotFoundError:
    # print("文件不存在!")
    pass
'''
try:
	with open('book') as f:
		contents=f.read()
except FileNotFoundError:
	print("sorry ,this file does not exit.")
else:
	words_num=contents.lower().count('the')
	print(words_num)