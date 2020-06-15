#coding:utf-8
#第1题双链表

class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkList:
    def __init__(self):
        self.head = Node(None)
        self.length = 0

    def headInsert(self,node):
        myNode = Node(node)
        myNode.next = self.head
        self.head.prev = myNode
        self.head = myNode
        self.length = self.length + 1

    def insert(self,poscation,node):
        if poscation is None or poscation<= 0:
            self.headInsert(node)
        else:
            myNode = Node(node)
            count = 0
            curent = self.head
            while count < poscation - 1:
                count = count + 1
                curent = curent.next
            myNode.next = curent.next
            curent.next.prev = myNode
            myNode.prev = curent
            curent.next = myNode
            self.length = self.length + 1


