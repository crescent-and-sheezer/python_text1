# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/17 9:54
# @File: 1.py
# message = "hello world"
# print(message)
# message = "hello"
# print(message)
# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/19 14:13
# @File: 2.1.py
嘉宾名单=['小可','小林','小本','小小']
print(嘉宾名单)
print(嘉宾名单[1]+"有事不能来赴约")
嘉宾名单.remove('小林')                    #方法remove（）用于删除元素，根据值删除元素
嘉宾名单.append('小王')                    #方法append（）用于添加元素
print(嘉宾名单)
print("我找到了一个更大的餐桌，我想加几个人")
嘉宾名单.insert(0,'小埋')                  #方法insert（）用于插入元素
嘉宾名单.insert(2,'小爱')
嘉宾名单.append('小年')
print(嘉宾名单)
print("新餐桌无法送来，只能请两个朋友")
嘉宾名单.pop(1)                           #方法pop（）用于删除元素，类似于栈顶被弹出，也可利用索引弹出任何位置的值
print("抱歉，临时有事无法邀请你来聚餐")
嘉宾名单.pop(1)
print("抱歉，临时有事无法邀请你来聚餐")
嘉宾名单.pop(1)
print("抱歉，临时有事无法邀请你来聚餐")
嘉宾名单.pop(1)
print("抱歉，临时有事无法邀请你来聚餐")
嘉宾名单.pop(1)
print("抱歉，临时有事无法邀请你来聚餐")
print(嘉宾名单)
print("请来参加我的聚餐")
del 嘉宾名单[0]                          #使用del语句删除元素，条件是要知道其索引
del 嘉宾名单[0]
print(嘉宾名单)