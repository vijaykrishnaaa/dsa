class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self,data):
        new_node=Node(data)
        self.top=new_node
        self.heigth=1

    def printstack(self):
        temp=self.top
        while(temp):
            print(temp.data,end="\n")
            temp=temp.next
    def push(self,data):
        new_node=Node(data)
        if self.heigth==0:
            self.top=new_node
            self.heigth=1
        new_node.next=self.top
        self.top=new_node
        self.heigth+=1
    def pop(self):
        if self.heigth==0:
            return "Stack is empty"
        temp=self.top
        self.top=self.top.next
        self.heigth-=1
Box=Stack(1)
Box.push(2)
Box.push(3)
Box.push(4)
Box.push(5)
Box.push(6)
Box.pop()
Box.pop()
Box.printstack()