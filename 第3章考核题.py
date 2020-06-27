#coding:utf-8

'''
第1题
'''
# def juege(data):
#     st = 'abcdefghigklmnopqrstuvwxyz'
#     num = '0123456789'
#     for i in data.lower():
#         if (i in st) or (i in num):
#             continue
#         else:
#             return False
#     return True

# print(juege('Hgegg'))
# print(juege('hashguHHHGu455$'))

'''
第2题
'''

# from datetime import datetime,timedelta
# start = '2019-12-25'
# end = '2020-01-10'
# start_date = datetime.strptime(start,r'%Y-%m-%d')
# end_date = datetime.strptime(end,r'%Y-%m-%d')
# while start_date <= end_date:
#     print(start_date.strftime(r'%Y-%m-%d'))
#     start_date += timedelta(days=1)

'''
第3题；点x = (5, 6, 7)和y = (8, 9, 9)之间的距离
'''
# x = (5,6,7)
# y = (8,9,9)
# dis = ((y[0]-x[0])**2 +(y[1]-x[1])**2 +(y[2]-x[2])**2)**0.5
# print('x（5，6，7）和y(8,9,9)的距离为{0:.1f}'.format(dis))

'''
第4题
'''
# number = 6
# res = 1
# while number > 0:
#     res = res * number
#     number = number - 1
# outnumber = 0
# for i in str(res):
#     outnumber = outnumber + int(i)
# print(outnumber)

'''
第5题
'''
# def fib(n):
#     a, b = 0, 1
#     assert n>=0
#     assert type(n) == int
#     while n > 0:
#         a, b = b, a + b
#         n = n - 1
#         yield a

# n = int(input('请输入要获取前多少项斐波那契数列:'))
# for i in fib(n):
#     print(i)

# def fib2(n):
#     assert n>=0
#     a,b = 0,1
#     while n > 0:
#         a,b = b,a+b
#         n = n - 1
#         print(a)
# fib2(5)