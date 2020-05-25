#coding:utf-8

'''
以姓名+年龄/出生时间创建对象，通过方法得到当前年龄
'''
import datetime

class Age:
    '''
    计算年龄，实例化需要定义姓名，年龄/出生年月
    '''
    def __init__(self,name,**kwargs):
        self.name = name
        self.age = kwargs.get('age')
        self.birth = kwargs.get('birth')

    def circleAge(self):
        if self.birth:
            nowtime = datetime.date.today().year
            self.age = nowtime - self.birth
        return self.age

rico = Age('rico',age=25)
bolo = Age('bolo',birth=1994)
print(rico.circleAge())
print(bolo.circleAge())