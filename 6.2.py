# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/23 15:37
# @File: 6.2.1.py

'''
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name,languages in favorite_languages.items():
    print(name.title()+" "+languages.title())
'''
'''
rivers={'a':'ngg','b':'nnn','nile':'egypt'}
for river,value in rivers.items():
    print("The "+river.title()+" runs through "+value.title()+".")
for river in rivers.keys():
    print(river)
for value in rivers.values():
    print(value)
'''
#注意这道题你没写对
favorite_languages={
        'jen':'python',
        'sarah':'c',
        'daming':'java',
        'sam':'c++',
}
people={'tom','sam','daming','lingling'}
for man in people:
    if man in favorite_languages.keys():
        print("thanks "+man)
    else:
        print("would you like to join us? "+man)