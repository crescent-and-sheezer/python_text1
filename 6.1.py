# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/23 14:37
# @File: 6.1.py

'''
Friend={'first_name':'he','last_name':'yan','age':'25','city':'shanghai'}
print(Friend)
'''
'''
numbers={'vv':2,'cc':6,'tt':4,'xf':7,'yy':39}
print(numbers)
for number in numbers:
    print(number.title()+",do you like the number?")
'''
words = {
    'dog': 'wangwang',
    'cat': 'miaomiao',
    'bird': 'jiji',
    'dragon': 'wawa',
}
for word in words:
    print(word + " : " + words[word])

for word in words:
    print(word + "\n\t" + words[word])
