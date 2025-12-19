class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(10)
b=Node(20)
c=Node(30)

a.next=b
b.next=c
head=a

def reverse(head):
    curr=head
    prev=None

    while curr:
        next=curr.next 
        curr.next=prev
        prev=curr
        curr=next

    head = prev
    return head

def recursivereverse(head):
    if head is None or head.next is None:
        return head
    newhead=recursivereverse(head.next)
    head.next.next=head
    head.next=None
    return newhead

def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")

head=recursivereverse(head)
display(head)