#coding:utf-8

contryandcity = {'中国':'北京','法国':'巴黎','美国':'纽约',
'英国':'伦敦','日本':'东京'}

contry = input("请问需要查阅哪个国家的首都：")
print("{0}的首都是{1}".format(contry,contryandcity[contry]))