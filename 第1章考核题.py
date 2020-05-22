#coding:utf-8

#下面为第一章测试题答案

'''
第1题
'''
st = 'python'
x0 = st[0]
x1 = st[1]
x2 = st[2]
x3 = st[3]
x4 = st[4]
x5 = st[5]
#print(x0,x1,x2,x3,x4,x5)

'''
第2题
'''
def avr (sc):
    sc.sort()
    sc.pop(0)
    sc.pop(-1)
    return 'Score is {0:.1f}'.format((sum(sc))/len(sc))

#scoreLst = [9.9, 9.2, 8.1, 9.7, 10, 8.3, 8.6, 9.5, 8.4]
#print(avr(scoreLst))    

'''
第3题
'''
def valLim(di):
    revdi = {v:k for k,v in di.items()}
    limval = sorted(revdi)[0]
    print("最小的键值对是'{0}:{1}'".format(revdi.get(limval),limval))

#d = {'huawei': 91.2, 'alibaba': 94.1, 'qq':90.1, 'baidu':89.4, 'xiaomi':88.4}
#valLim(d)

'''
第4题
'''
def flrange(start,end,step):
    '''
    flrange(start,end,step)，产生正数等差数列，支持浮点数
    start：数列最小值
    end：数列最大值，需要比最小值大,生成的等差数列最大值小于end
    step：步长，可以为整数，也可以为小数
    '''
    from decimal import Decimal

    arrlist = []
    i = start
    if step < 0:
        print("步长必须为正数")
    else:
        while i < end:
            arrlist.append(i)
            i = float(Decimal(str(i)) + Decimal(str(step)))
        return arrlist

#print(flrange(-1.5,1,-0.1))

'''
第5题
'''
def gravity(g):
    def weight(m):
        return m*g
    return weight
# gLoc = gravity(9.78046)
# print(gLoc(2))

'''
第6题
'''
def fac (n):
    '''
    fac(n)计算n的阶乘，注意n需要大于0且为正整数
    '''
    rst = 1
    for i in range(1,n+1):
        rst = rst*i
    return rst

# print(fac(4))

'''
第7题
'''
# filetype = ('.jpg','.gif','.png')
# fil = ['a.py', 'b.jpg', 'c.gif', 'd.map', 'e.png', 'f.jpg', 'k.txt', 'f.gif', 'h.png', 'm.docx']
# #使用列表choseFile存储取出的文件
# choseFile =[]
# for i in filetype:
#     for j in fil:
#         if i in j:
#             choseFile.append(j)
# print(choseFile)

'''
第8题
'''
orangeList = [1, "a", 2, "b", 3, "c", 4, "d"]
orangeVal = orangeList.copy()
orangeVal.pop(0)
newdic= dict()
for i in range(len(orangeList)):
    if (i+1)%2 == 1:
        newdic[orangeList[i]] = orangeVal[i]
print(newdic)
