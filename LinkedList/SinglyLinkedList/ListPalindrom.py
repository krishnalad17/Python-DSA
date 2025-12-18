class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(10)
b=Node(20)
c=Node(30)

a.next=b
b.next=c
c.next=b
head=a

def palindrom(head):
    stack=[]
    temp=head
    while temp:
        stack.append(temp.data)
        temp=temp.next
    temp=head
    while temp:
        if stack.pop()!=temp.data:
            return False
        temp=temp.next
    return True

def palindrom1(head):
    stack=[]
    slow=head
    fast=head
    while fast and fast.next:
        stack.append(slow.next)
        slow=slow.next 
        fast=fast.next.next 
    #skip middle element 
    if fast:
        slow=slow.next
    while slow:
        if slow.data!=stack.pop():
            return False
        slow=slow.next
        return True

print(palindrom1(head))