#coding:utf-8
import calendar

year = int(input("请输入年份："))
month = int(input("请输入月份："))
today = int(input("请输入具体哪一号："))
lastday = calendar.monthrange(year, month)[1]

print('本月最后一天是{0}月{1}日，本月有{2}天'.format(month,lastday,lastday))