# _*_ coding:utf-8
# 作者:凡
# @Time: 2021/2/11 16:33
# @File: alice.py
def count_words(filename):

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry,the file " + filename + " does not exist."
        print(msg)
        # pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
filenames = ['alice','why','guest','cc']
for filename in filenames:
    count_words(filename)