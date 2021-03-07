# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/20 20:36
# @File: 3.py

'''
#使用sort()对队列进行永久性排序
cars=['bmw','audi','toyato','subaru']
print(cars)
cars.sort()
print(cars)
##sort()方法永久性对列表按字母顺序进行排列，再也无法恢复
#按字母顺序相反的进行排序
cars.sort(reverse=True)
print(cars)
##向sort()方法内传递参数reverse=True
#使用函数sorted()对列表进行临时排列
cars=['bmw','audi','toyato','subaru']
print(sorted(cars))
print(cars)
##所以sorted()函数不改变列表原来的排列顺序
##注意啊，老哥 sorted()是函数啊  所以列表的元素要传入函数里呀
print(sorted(cars,reverse=True))
print(cars)
##相反顺序排列向sorted()函数里传入列表和reverse=True
##                       注意这里的易错点啦，sort()是方法，sorted()是函数，方法是调用，函数进行数据传递
'''
l=['b','c','e','a','f']
print(l)
print(sorted(l))               #方法sort（）对列表进行永久性排序
print(l)
print(sorted(l,reverse=True))  #函数sorted()对列表进行临时排列   （sort()是方法，sorted()是函数，方法是调用，函数进行数据传递）
print(l)
l.reverse()                    #方法reverse（）对列表进反向打印
print(l)
l.reverse()
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
