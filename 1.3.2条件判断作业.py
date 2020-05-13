#coding:utf-8
'''
题目：判断键盘输入，数字则扩大十倍，字母则尾缀加@python后打印
其他情况则将输入内容原样显示
'''
idata = input("请输入内容：")
if idata.isnumeric():
    print(10*int(idata))
elif idata.isalpha():
    print(idata+"@python")
else:
    print(idata)

'''
习题课后查找资料对比判断字符串是否为数字字符串函数
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）
'''