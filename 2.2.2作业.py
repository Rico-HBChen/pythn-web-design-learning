#coding:utf-8
class Rectangle:
    def __init__(self):
        self.width = 0
        self.length = 0

    def __getattr__(self,name):
        if name == 'size':
            return self.width,self.length
        else:
            raise AttributeError

    def __setattr__(self,name,value):
        try:
            if name == 'size':
                self.width,self.length = value
            else:
                self.__dict__[name] = value
        except TypeError:
            print('size需要输入长和宽，中间用逗号隔开。')

rect = Rectangle()
rect.width = 5
rect.length =3
rect.size = 20，30
print(rect.size)