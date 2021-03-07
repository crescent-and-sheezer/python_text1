# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/12 17:45
# @File: 11.1.py
'''
import unittest
from city_function import city_functions
class test(unittest.TestCase):
    def test1(self):
        city_country = city_functions('santiago','chile')
        self.assertEqual(city_country,'Santiago Chile')

unittest.main()
'''
import unittest
from city_function import city_functions
class test(unittest.TestCase):
    def test1(self):
        city_country = city_functions('santiago','chile')
        self.assertEqual(city_country,'Santiago Chile')

    def test2(self):
        city_country_population = city_functions('santiago','chile','population=5000000')
        self.assertEqual(city_country_population,'Santiago Chile Population=5000000')
unittest.main()