# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/12 20:49
# @File: 11.2.1.py
# testEmployee.py
import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.test_employee = Employee('zhang', 'chenchen', 13000)

    def test_give_default_raise(self):
        self.test_employee.give_raise(8000)

    def test_give_custom_raise(self):
        self.test_employee.give_raise()


unittest.main()