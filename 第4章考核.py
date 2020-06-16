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