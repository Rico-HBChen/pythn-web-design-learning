#coding:utf-8

# class Things:
#     '''
#     定义商品价格，折扣，最低折扣数量
#     '''
#     def __init__(self,price,discont,limNum):
#         self.number = 0
#         self.price = price
#         self.discont = discont
#         self.discontNumber = limNum
#         self.SumSels = 0
#         self.SumNumber = 0
    
#     def sels(self,number):
#         assert number > 0
#         self.SumNumber = self.SumNumber + number
#         if number >= self.discontNumber:
#             self.SumSels = self.price * number * self.discont
#         else:
#             self.SumSels = self.price * number
#         return '''当前销售数量是：{nownum}，当前销售额是：
#         {mony}'''.format(nownum=self.SumNumber,mony=self.SumSels)
    
#     def get_number(self):
#         return self.SumNumber

#     def get_money(self):
#         return self.SumSels

# book = Things(12,0.5,5)
# book.sels(3)
# print(book.get_number())
# print(book.get_money())

# book.sels(6)
# print(book.get_number())
# print(book.get_money())

'''
第2题
'''
# def delt2zero(num):
#     '''
#     生成器
#     '''
#     assert type(num) is int
#     assert num > 0
#     nxt = num
#     while nxt>0:
#         nxt = nxt - 1
#         if num == 0:
#             break
#         yield nxt

# f = delt2zero(8)
# print(list(f))

#迭代器写法
# class d2z:
#     def __init__(self,n):
#         assert n > 0
#         assert type(n) is int
#         self.number = n
#         self.result =[n]
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         while self.number > 0:
#             self.number = self.number -1
#             self.result.append(self.number)
#         return self.result

# exp = d2z(6)
# print(exp.__next__())


'''
第3题，生成名人名言的类
'''
# import random

# class Notes:
#     '''
#     随机产生一句名人名言，不用传入任何参数。
#     '''
#     def __init__(self):
#         dataSum = ['子曰：学而时习之，不亦说乎',
#     '李白：安能摧眉折腰事权贵，使我不得开心颜','刘禹锡:山不在高,有仙则名;水不在深,有龙则灵']
#         self.val = str(random.sample(dataSum,1))
    
#     def __str__(self):
#         return self.val
#     __repr__ = __str__

# w = Notes()
# print(w)

'''
第4题，生成物理学家的类
'''

class Physicist:
    '''
    判断是否为物理学家，实例化参数为研究方向的英文名称；
    输入实例名称，直接返回是否为物理学家的判断。
    '''
    def __init__(self,research):
        self.research = research
        self.is_physicist = True

    def __str__(self):
        if 'physics' in self.research:
            self.is_physicist = True
            return "是一个物理学家"
        else:
            self.is_physicist = False
            return "不是一个物理学家"
    __repr__ = __str__

rico = Physicist('physics')
print(rico)
print(rico.research)

'''
第5题
'''
class Temperature:
    '''
    温度转换类，根据所测中间物理量对应温度范围，得到最终温度范围;
    注意仅仅适用于线性变化情况。
    stader1为记录温度最小值和最大值的列表；
    stader2为记录所测物理量对应温度最小值和最大值的列表。
    例如：
    温度传感器所测温度范围是0-50摄氏度，对应电压10-2000毫安，
    要得到该传感器电压对应温度的类，可以用如下方法：
    senser1 = Temperature([0,50],[10,2000])
    得到电压1000毫安对应温度值写法：
    senser1.get_temperature(1000)
    '''
    def __init__(self,stander1,stander2):
        self.stander1 = stander1
        self.stander2 = stander2

    def get_temperature(self,test_data):
        tmp_mini = self.stander1[0] #温度范围最小值
        tmp_max = self.stander1[1] #温度范围最大值
        testing_mini = self.stander2[0] #测量的物理量最小值
        testing_max = self.stander2[1] #测量的物理量最大值
        temperature = tmp_mini + (test_data - testing_mini)*(tmp_max-tmp_mini)/(testing_max-testing_mini)
        return float("{0:.1f}".format(temperature))

senser1 = Temperature([0,50],[10,2000])
print(senser1.get_temperature(1000))