# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/1/27 11:20
# @File: 7.3.py
'''
# 我的做法
sandwich_orders = ['aa','bb','vv','tuna','gg']
finished_sandwiches = []
while sandwich_orders:
    order=sandwich_orders.pop()
    print(order.title()+" is making sandwich.")
    finished_sandwiches.append(order)
print("\nwe finished your sandwich.")
# for finished_sandwiche in finished_sandwiches:
print(finished_sandwiches)
# 别人的做法
sandwich_orders=['orange','banana','apple']
finished_sandwichs=[]
while sandwich_orders:
	for order in sandwich_orders:
		print(order+" is making .")
		finished_sandwichs.append(order)
		sandwich_orders.remove(order)
print("your order is finished.")
print(finished_sandwichs)
'''
'''
# 我的做法
sandwich_orders = ['aa','bb','pastrami','vv','pastrami','tuna','gg','pastrami']
finished_sandwiches = []
print("'pastrami' is out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    order=sandwich_orders.pop()
    print(order.title()+" is making sandwich.")
    finished_sandwiches.append(order)
print("\nwe finished your sandwich.")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
# 别人的做法
sandwich_orders=['orange','pastrami','banana','apple','pastrami']
finished_sandwichs=[]
print("The pastrami has been sale off.")
while sandwich_orders:
	for order in sandwich_orders:
		if order!='pastrami':
			print(order+" is making .")
			finished_sandwichs.append(order)
			sandwich_orders.remove(order)
		else:
			sandwich_orders.remove(order)
			continue
print("your order is finished.")
print(finished_sandwichs)
'''
prompts = {}
active = True
while active:
    name = input("Please tell me you name: ")
    prompt = input("\nIf you could visit one place in the world,where would you go?")
    prompts[name]=prompt
    prompt1 =input("If you want to responses,please option 'yes',else please option 'no'.")
    if prompt1=='no':
        active=False
print("\n---Poll Results---")
for name,prompt in prompts.items():
    print(name + " would like to go to " + prompt +".")