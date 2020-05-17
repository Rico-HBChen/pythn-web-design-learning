#coding:utf-8


def distance(*location):
    '''
    习题1:计算平面两点距离
    '''
    d = ((location[2]-location[0])**2+(location[3]-location[1])**2)**0.5
    return d


def strtest(st,col):
    print(set(st))
    print(col)
    if set(st) & col :
        return True
    else:
        return False

x1=0
y1=0
x2=4
y2=3
# print(distance(x1,y1,x2,y2))

result = strtest('hello',{'a','b','c'})
print(result)