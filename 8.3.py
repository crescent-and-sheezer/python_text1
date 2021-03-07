# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/28 11:41
# @File: 8.3.py
'''
# 我的做法
def city_country(city_name,country_name="Chile"):
    fullname=city_name.title()+","+country_name.title()
    return fullname
Full_Name=city_country('Santiago')
print(Full_Name)
Full_Name=city_country('Santiago1')
print(Full_Name)
Full_Name=city_country('Santiago2')
print(Full_Name)
# 别人的做法
def city_country(city,country):
	message=city+','+country
	return message
ex1=city_country("金山屯","China")
ex2=city_country("New York","America")
ex3=city_country("Venice","Italy")
print(ex1)
print(ex2)
print(ex3)
'''
'''
# 我的做法
def make_album(musician_name,music_name,number=''):
    album={'musician':'musician_name','music':'music_name'}
    if number:
        album['number']=number
    return album
musician_music=make_album('zhoujielun','Mojito',number=1)
print(musician_music)
# 别人的做法
def make_album(song,album,amount=""):
	if amount:
		album={'song':song,'name':album,'amount':amount}
	else:
		album={'song':song,'name':album}
	return album
ex1=make_album('东风破','菊花台')
ex2=make_album('青花瓷','夜莺',30)
ex3=make_album("将军令",'花田',90)
print(ex1)
print(ex2)
print(ex3)
'''
# 注意，你没写出来
def make_album(song,album,amount=""):
	if amount:
		album={'song':song,'name':album,'amount':amount}
	else:
		album={'song':song,'name':album}
	return album
while True:
	print("\nPlease enter the song ,album: ")
	song=input("Enter your song name: ")
	album=input("Enter your album name: ")
	if song=='quit' and album=='quit':
		break
	else:
		solution=make_album(song,album)
		print(solution)