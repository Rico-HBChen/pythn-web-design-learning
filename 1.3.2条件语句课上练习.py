#coding:utf-8
#判断输入的数字是奇数还是偶数
number = int(input("请输入要判断奇偶的数："))
if number % 2 == 0:
    print("{0}是偶数".format(number))
else:
    print("{0}是奇数".format(number))