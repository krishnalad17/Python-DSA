class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(10)
b=Node(20)
c=Node(30)
d=Node(40)

a.next=b
b.next=c
c.next=d
head=a

def deletemiddle(head):
    slow=head
    fast=head
    while fast and fast.next:
        fast=fast.next.next 
        slow=slow.next 
    slow.next=slow.next.next 
    return head

def display(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("None")

head=deletemiddle(head)
display(head)

