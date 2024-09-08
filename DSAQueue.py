class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self,data):
        new_node=Node(data)
        self.first=new_node
        self.last=new_node
        self.length=1
    def enqueuelast (self, data):
        new_node = Node(data)
        if self.first is None:
            self.first=new_node
            self.last=new_node
            self.length=1
        else:
            self.last.next=new_node
            self.last=new_node
            self.length+=1
    def enqueuefirst (self, data):
        new_node = Node(data)
        if self.first is None:
            self.first=new_node
            self.last=new_node
            self.length=1
        else:
            new_node.next=self.first
            self.first=new_node
            self.length+=1

    def dequeuefirst (self):
        if self.length==0:
            return "queue is empty"
        if self.length==1:
            self.first=None
            self.last=None
        else:
            temp=self.first
            self.first=self.first.next
            temp.next=None
            self.length-=1

    def dequeuelast (self):
        if self.length==0:
            return "queue is empty"
        if self.length==1:
            self.first=None
            self.last=None
        else:
            temp=self.first
            while self.last!=temp.next:
                temp=temp.next
            temp.next=None
            self.last=temp
            self.length-=1

            
    def printqueue(self):
        temp=self.first
        while(temp):
            print(temp.data, end="\n")
            temp=temp.next

QQ=Queue(1)
QQ.enqueuelast(2)
QQ.enqueuelast(3)
QQ.enqueuelast(4)
QQ.enqueuelast(5)
QQ.enqueuefirst(6)
QQ.dequeuefirst()
QQ.dequeuelast()
QQ.printqueue()