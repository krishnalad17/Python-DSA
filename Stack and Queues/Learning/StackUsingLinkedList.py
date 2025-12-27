class Node():
    def __init__(self,data):
        self.data=data 
        self.next=None

head=None

class Stack:
    def push(head,data):
        newnode=Node(data)
        if head is None:
            return newnode
        temp=head
        while temp.next:
            temp=temp.next 
        temp.next=newnode
        return head
    
    def pop(head):
        if head is None:
            return None
        temp=head
        while temp.next.next:
            temp=temp.next 
        temp.next=None
        return head
    
    def peek(head):
        if head is None:
            return None
        temp=head
        while temp.next:
            temp=temp.next 
        return temp.data
    
    def isEmpty(head):
        return head if head is head else None
    
    def display(head):
        temp=head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")

s=Stack()
head=s.push(head,1)
head=s.push(head,2)
head=s.push(head,3)
