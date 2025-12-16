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

def insertfirst(head,data):
    newnode=Node(data)
    if head is None:
        newnode=head
        return newnode
    newnode.next=head
    head=newnode
    return head

def insertatlast(head,data):
    newnode=Node(data)
    if head is None:
        newnode=head
        return newnode
    temp=head
    while temp.next:
        temp=temp.next 
    temp.next=newnode
    return head

def insertatposition(head,data,k):
    newnode=Node(data)
    temp=head
    count=1
    while temp is not None and count<k-1:
        temp=temp.next 
        count+=1
    newnode.next=temp.next 
    temp.next.next.prev=newnode
    newnode.prev=temp
    temp.next=newnode
    return head

def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")
    
head=insertfirst(head,5)
head=insertatlast(head,40)
head=insertatposition(head,35,4)
display(head)