# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/12 20:50
# @File: employee.py

class Employee():
	def __init__(self,firstname,lastname,salary):
		self.firstname=firstname
		self.lastname=lastname
		self.salary=int(salary)
	def give_raise(self,increase=''):
		if increase!='':
			self.salary+=int(increase)
		else:
			self.salary+=5000