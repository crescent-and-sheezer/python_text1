# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/12 17:42
# @File: city_function.py
def city_functions(city,country,population=''):
    if population:
        T = city + ' ' + country + ' ' + population
    else:
        T = city + ' ' + country
    return T.title()