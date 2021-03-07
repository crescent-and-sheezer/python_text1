# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/23 16:57
# @File: 6.3.py

'''
friend={'first_name':'he','last_name':'yan','age':'25','city':'shanghai'}
friend1={'first_name':'wu','last_name':'ben','age':'23','city':'beijing'}
friend2={'first_name':'ke','last_name':'jie','age':'26','city':'nanjing'}
peoples=[friend,friend1,friend2]
for people in peoples:
    print(people)
'''
'''
kiki={'type':'dog','master_name':'Ben'}
sun={'type':'cat','master_name':'Ken'}
han={'type':'pig','master_name':'Nan'}
lisa={'type':'fish','master_name':'Ran'}
pets=[kiki,sun,han,lisa]
for pet in pets:
    print(pet)
'''
'''
#注意这道题没做出来，是翻了书的
favorite_places={
    'Ken':['nanjing','wuhan','shanghai'],
    'Ben':['beijing','tianjing'],
    'Jon':['zhejiang','jiujiang'],
}
for friend_name,places in favorite_places.items():
    print("\n"+friend_name.title()+"最喜欢的地方：")
    for favorite_place in places:
        print(favorite_place.title())
'''
'''
favorite_numbers={
    'Ken':[1,5,3,6,7,4],
    'Ben':[3,5,9,0],
    'CC':[7,3,9],
}
for friend,numbers in favorite_numbers.items():
    print("\n"+friend.title())
    for number in numbers:
        print(number)
'''
#注意这道题，不仅做错了，也理解错了意思
cities = {
    'dezhou': {
        'country': 'china',
        'population': '13 billion',
        'fact': 'great',
    },
    'newyork': {
        'country': 'america',
        'population': '3 billion',
        'fact': 'wide',
    },
    'dongjing': {
        'country': 'japan',
        'population': '1 billion',
        'fact': 'little',
    },
}
for city_name, city_info in cities.items():
    print('\n\tcity name: ' + city_name)
    print("\tcountry: " + city_info['country'])
    print("\tpopulation: " + city_info['population'])
    print("\tfact: " + city_info['fact'])
