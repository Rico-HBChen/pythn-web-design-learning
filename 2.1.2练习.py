#coding:utf-8

'''
网购图书费用计算类，假设费用超过100则包邮
'''

class SumPay:
    def Circulate(self,shopList):
        pay = 0
        for i in shopList.items():
            pay = pay + i[1][0]*i[1][1]
        if pay > 100:
            return pay
        else:
            return pay+5

customer = SumPay()
buy ={'python':[24,1],'java':[55,1],'c':[46,2]}
print(customer.Circulate(buy))