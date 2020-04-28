#coding:utf-8
'''第1章字符串’you need python'操作
- 分别得三个单词
- 从左到右，隔字符取一个
- 从右到左，隔字符取一个
- 将字符串反序
'''
strTest = 'you need python'
print("如下为将字符串分割为三个单词的结果：")
print(strTest[:3] + '\n' + strTest[4:8] + '\n' + strTest[9:])
print("如下为从左到右，隔字符取")
print(strTest[::2])
print("如下为从右到做隔字符取")
print(strTest[::-2])
print("如下为字符串反序")
print(strTest[::-1])