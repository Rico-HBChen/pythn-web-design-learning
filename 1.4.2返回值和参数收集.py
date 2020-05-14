#coding:utf-8
import random

#例1，斐波那契数列前n项
def fb(n):
    '''
    显示斐波那契数列前n项，n大于等于3
    '''
    fblst=[0,1]
    for i in range(n-2):
        fblst.append(fblst[-1]+fblst[-2])

    '''        
    back = [fblst.append(fblst[-1]+fblst[-2])  for i in range(n-2)]
    '''
    return fblst

#例2
def ran_num():
    '''
    在0-100随机区10000个整数，组成数组后取所有数平均数和标准差
    '''
    data = []
    for i in range(10000):
        data.append(random.randint(0,100))
    avr = sum(data)/len(data)
    sum2 = 0
    for i in data:
        sum2 = sum2 + (i-avr)**2 
    sn = (sum2/len(data))**0.5
    return data,avr,sn

#anser = random.randint(1,100)
a,b,c =ran_num()
print(a)
print(b)
print(c)
