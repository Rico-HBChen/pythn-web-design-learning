#coding:utf-8

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
print(fb(5))
