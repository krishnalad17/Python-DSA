class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

a=Node(10)
b=Node(20)
c=Node(30)

a.next=b
b.prev=a
b.next=c
c.prev=b
head=a

def reverse(head):
    if head is None:
        return None
    temp=head
    curr=None

    while temp:
        curr=temp.prev
        temp.prev=temp.next 
        temp.next=curr
        temp=temp.prev
    
    head=curr.prev         
    return head

def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")

head=reverse(head)
display(head)