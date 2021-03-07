# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/21 16:37
# @File: 4.2.1.py

'''
for value in range(1,21):
    print(value)
'''
'''
for value in range(1,1000001):
    print(value)
    

numbers=list(range(1,1000001))
for number in numbers:
    print(number) 
'''
'''
ls=[]
for value in range(1,1000001):
    l=value
    ls.append(l)
print(min(ls))
print(max(ls))
print(sum(ls))
'''
'''
Ns=list(range(1,21,2))
for N in Ns:
    print(N)
'''
'''
Numbers=list(range(3,31,3))
for Number in Numbers:
    print(Number)
'''
'''
number3s=[value**3 for value in range(1,11)]
for number3 in number3s:
    print(number3)

numbers=list(range(1,11))
for value in numbers:
    number=value**3
    print(number)
'''

list=[n**3 for n in range(1,11)]
print(list)