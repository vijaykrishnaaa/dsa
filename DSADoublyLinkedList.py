class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLinkedlist:
    def __init__ (self,data):
        new_node=Node(data)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def append (self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.length=1
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.length+=1
    def prepend(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.length=1
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
            self.length+=1
    def popfirst (self):
        if self.length==0:
            return None
        self.head=self.head.next
        self.head.prev=None
        self.length-=1
    def poplast (self):
        if self.length==0:
            return None
        self.tail=self.tail.prev
        self.tail.next=None
        self.length-=1
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _  in range(index):
            temp=temp.next
        return temp
    def set (self,data,index):
        temp=self.head
        if index<0 or index>=self.length:
            return None
        for _ in range (index):
            temp=temp.next
        temp.data=data
    def insert (self,data,index):
        if index<0 or index>self.length:
            return None
        temp=self.get(index-1)
        new_node=Node(data)
        new_node.prev=temp
        new_node.next=temp.next
        temp.next=new_node
    def remove (self,index):
        if index==0:
            self.popfirst()
        if index==self.length:
            self.poplast()
        if index<0 or index>self.length:
            return None
        temp=self.get(index-1)
        main=self.get(index+1)
        temp.next=main
        main.prev=temp
    def reverse (self):
        temp=None
        current=self.head
        self.head , self.tail =self.tail , self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
            
            

        
        

        
        


DLL=DLinkedlist(7)
DLL.append(8)
DLL.append(3)
DLL.prepend(2)
DLL.prepend(5)
DLL.set(4,1)
DLL.insert(9,2)
DLL.remove(5)
DLL.printlist()
DLL.reverse()
DLL.printlist()
print(DLL.get(1))