# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/26 18:02
# @File: 7.2.1.py
'''
prompt = "\nPlease you tell me,what do you need?"
prompt += "\nEnter 'quit',you can over the prompt."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
'''
'''
pronpt = "Please tell me your age:"
while True:
    age = input(pronpt)
    if age != 'exit':
        if int(age) < 3:
            print("You can free.")
        elif int(age) >= 3 and int(age) <= 12:
            print("You need to pay 10 $.")
        elif int(age) > 12:
            print("You need to pay 15 $.")
    else:
        break
'''
'''
#使用条件测试来结束循环
message=""
while message!=0:
	message=input("Enter your age please: ")
	message=int(message)
	if message!=0:
		if message<=3:
			print("price=0")
		elif message<12:
			print("price=$10")
		else:
			print("price=$15")
'''
'''
message=""
active=True
while active:
	message=input("Enter your age please: ")
	message=int(message)
	if message==0:
		active=False
	else:
		if message<=3:
			print("price=0")
		elif message<12:
			print("price=$10")
		else:
			print("price=$15")
'''

message=""
while True:
	message=input("Enter your age please: ")
	if message=='quit':
		break
	else:
		message=int(message)
		if message<=3:
			print("price=0")
		elif message<12:
			print("price=$10")
		else:
			print("price=$15")