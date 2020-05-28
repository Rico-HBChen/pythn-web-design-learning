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
class d2z:
    def __init__(self,n):
        assert n > 0
        assert type(n) is int
        self.number = n
        self.result =[n]
    
    def __iter__(self):
        return self

    def __next__(self):
        while self.number > 0:
            self.number = self.number -1
            self.result.append(self.number)
        return self.result

exp = d2z(6)
print(exp.__next__())