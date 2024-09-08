class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self, data):
        new_node=Node(data)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="-->")
            temp=temp.next
        print("null")
    def append (self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
            self.tail=new_node
        else:
            new_node=Node(data)
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def poplist (self):
        if self.length==0:
            return None
        pre=self.head
        temp=self.head
        while temp.next is not None:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
            return temp
    def prepend (self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
            self.tail=new_node
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    def popfirst(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=0
    def get (self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    def set (self,index,data):
        temp=self.get(index)
        if temp is not None:
            temp.data=data
            return True
        return False
    def insert(self,data,index):
        if index<0 or index>=self.length:
            return False
        new_node=Node(data)
        if index==0:
            self.prepend(data)
        if index==self.length-1:
            self.append(data)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return temp
    def remove(self,index):
        if index>0 or index>=self.length:
            return None
        if index==0:
            self.popfirst()
        if index==self.length-1:
            self.poplist()
        pre=self.get(index-1)
        temp=pre.next
        pre.next=temp.next
        temp.next=None
        self.length-=1
        return temp
    def reverse (self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after


ll=Linked_list(2)
ll.append(3)
ll.append(4)
ll.poplist()
ll.prepend(7)
ll.popfirst()
ll.prepend(6)
ll.set(2,9)
ll.prepend(1)
ll.insert(89,1)
ll.remove(1)
ll.reverse()
print(ll.get(2).data)
ll.printlist()
