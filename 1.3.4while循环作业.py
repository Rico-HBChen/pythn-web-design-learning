#coding:utf-8
import random

anser = random.randint(1,100)
guest = int(input("请猜一猜，我现在想的是哪个数？"))
while anser != guest:
    if guest > anser:
        print("哈哈，你猜的数太大了！")
    elif guest < anser:
        print("哈哈，你猜的数太小了！")
    else:
        break
    guest = int(input("再猜一猜吧！"))
else:
    print("恭喜你，猜对了我想的就是{0}".format(guest))