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