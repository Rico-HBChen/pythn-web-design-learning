#coding:utf-8

#例题1
def find_susu(x,y):
    '''
     find_susu(x,y)查找从x到y范围内的素数
    '''
    susu_list =[]
    for i in range(x if x>2 else 2,y+1):
        for j in range(2,i):
            for k in range(2,i):
                if j*k == i:
                    break
        else:
            susu_list.append(i)
    if len(susu_list) == 0:
        return "这个范围没有素数！"
    else:
        return susu_list

#作业
def upordown(x,y):
    '''
    upordown(x[,y])，x为要转换的单词
    y为1时转换为小写，y为2或缺省时
    转换为大写
    '''
    if y == 1:
        return x.lower()
    else:
        return x.upper()
print(upordown('Hello',2))