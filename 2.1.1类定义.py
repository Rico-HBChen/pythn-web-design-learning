#coding:utf-8

# class superMan:
#     '''
#     a class of superman
#     '''
#     def __init__(self,name):
#         self.name = name
#         self.kongfu = "xianglongshibazhang"
#     def done(self):
#         return "coding"
    
'''
创建1个反映学生基本属性和方法的类并实例化
'''
class Student:
    '''
    学生类，具备表示科目的属性subject，学号的属性ID,计算学生平均成绩的方法avrscore()
    '''
    def __init__(self,ID):
        self.subject = ['语文','数学','英语']
        self.ID = ID
    
    def avrscore(self,numberlst):
        return sum(numberlst)/len(numberlst)

rico = Student('0114')
print(rico.subject)
sc = [89,88,87,85]
print("平均分是：{0:.1f}".format(rico.avrscore(sc)))