#coding:utf-8
#第1题双链表

# class Node:
#     def __init__(self,data,prev=None,next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next

# class DoubleLinkList:
#     def __init__(self):
#         self.head = Node(None)
#         self.length = 0

#     def headInsert(self,node):
#         myNode = Node(node)
#         myNode.next = self.head
#         self.head.prev = myNode
#         self.head = myNode
#         self.length = self.length + 1

#     def insert(self,poscation,node):
#         if poscation is None or poscation<= 0:
#             self.headInsert(node)
#         else:
#             myNode = Node(node)
#             count = 0
#             curent = self.head
#             while count < poscation - 1:
#                 count = count + 1
#                 curent = curent.next
#             myNode.next = curent.next
#             curent.next.prev = myNode
#             myNode.prev = curent
#             curent.next = myNode
#             self.length = self.length + 1

#第2题
# import random
# lists = []
# for i in range(50):
#     lists.append(random.randint(0,100))
# print('原始数组为:{0}'.format(lists))
# list_chose = [i for i in lists if (i>=0 and i <=15) or (i>=25 and i<=50) or (i>=60 and i<=100)]
# print('乱序数组为:{0}'.format(list_chose))

# def rank1(list_orange):
#     list_ranked = list_orange
#     for i in range(len(list_ranked)):
#         for j in range(i+1,len(list_ranked)):
#             if list_ranked[i] > list_ranked[j]:
#                 list_ranked[i],list_ranked[j] = list_ranked[j],list_ranked[i]
#     return list_ranked

# def rank2(list_orange):
#     list_ranked = list_orange
#     for i in range(len(list_ranked)):
#         for j in range(len(list_ranked)-i-1):
#             if list_ranked[j] > list_ranked[j+1]:
#                 list_ranked[j],list_ranked[j+1] = list_ranked[j+1],list_ranked[j]
#     return list_ranked

# print('方法1排序后数组为:{0}'.format(rank1(list_chose)))
# print('方法2排序后数组为:{0}'.format(rank2(list_chose)))

#第3题
# def merg_sort(lists):
#     if len(lists) <= 1:
#         return lists
#     middle = len(lists)//2
#     left_list = []
#     right_list = []
#     for i in lists[:middle]:
#         if i <= lists[middle]:
#             left_list.append(i)
#         else:
#             right_list.append(i)
#     for i in lists[middle+1:]:
#         if i <= lists[middle]:
#             left_list.append(i)
#         else:
#             right_list.append(i)
#     # print(left_list,right_list)
#     return merg_sort(left_list) + [lists[middle]] + merg_sort(right_list)

# lists = [(5,1),(3,2),(1,3),(2,4),(4,'a')]
# # from random import shuffle
# # shuffle(lists)
# # print(lists)
# print(merg_sort(lists))

#第6题
'''
假设轴线上的三个圆圈从上到下为A、C、G
左侧两个圆圈由上到下为B、E
右侧两个圆圈由上到下为D、F
'''
import copy
#以下为求解最短路径
def findCloestrout(inf,rout,S,U,cloest_rout):
    key_UtoS = {} #记录u的每个key到D点会通过哪个已经确定的最短路径，用于后面输出最短路线
    for key in U:
        for key2 in S:
            if key+key2 in rout:
                if rout[key+key2]+S[key2] <= U[key]: #保持存储最小值
                    U[key] = rout[key+key2]+S[key2]
                    key_UtoS[key] = key2
            elif key2+key in rout:
                if rout[key2+key]+S[key2] <= U[key]:
                    U[key] = rout[key2+key]+S[key2]
                    key_UtoS[key] = key2
            else:
                continue
    min_value = inf
    key_min = None
    for key in U: #找最小的路径
        if U[key]<min_value:
            min_value = U[key]
            key_min = key
    del U[key_min]#从未确定的最短路径集合删除可以确定的最短路径
    S[key_min] = min_value#添加已经确定的最短路径
    for num in range(len(cloest_rout)):
        if cloest_rout[num][-1] == key_UtoS[key_min]:
            temp_list = copy.deepcopy(cloest_rout[num])
            temp_list.append(key_min)
            cloest_rout.append(temp_list)

rout = {'AB':1,'AD':1.2,'BC':0.5,'BE':2,'CD':0.3,'CE':1.3,
        'CF':1.5,'DF':2,'EG':1,'FG':0.9}
rout_list = [('A','B',1),('A','D',1.2),('B','C',0.5),('B','E',2),
             ('C','D',0.3),('C','E',1.3),('C','F',1.3),('D','F',2),
             ('E','G',1),('F','G',0.9)]
 
inf = float('inf')#无穷大
cloest_rout = [['A']]
S = {'A':0}  #确定最短路径集合
U = {'B':inf,'C':inf,'D':inf,'E':inf,'F':inf,'G':inf} #未确定的最短路径集合
 
while(U != {}): #直到未确定最短路径为空，才最终确定完最短路径
    findCloestrout(inf,rout,S,U,cloest_rout)
print('起点到终点最短路径里程为：{0}公里，经过的点为{1}。'.format(S.get('G'),cloest_rout[6]))