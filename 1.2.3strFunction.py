#coding:utf-8
'''
- 去掉' hello '左右侧的空格
- ’you need python'中的空格以'*'取代
'''
str1 = ' hello '
str1Convent = ''.join(str1.split(' '))
str2 = 'you need python'
str2Convent = '*'.join(str2.split(' '))
print(str1Convent)
print(len(str1Convent))
print(str2Convent)