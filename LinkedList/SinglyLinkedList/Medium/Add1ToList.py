class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(1)
b=Node(9)
c=Node(9)
d=Node(9)

a.next=b
b.next=c
c.next=d
d.next=None
head=a

def reverse(head):
    prev=None
    cur=head 
    while cur:
        next=cur.next 
        cur.next=prev
        prev=cur
        cur=next
    head=prev
    return head

def add(head):
    head=reverse(head)

    carry=1
    cur=head
    prev=None

    while cur:
        total=cur.data+1
        cur.data=total%10
        carry=total//10
        prev=cur
        cur=cur.next 

        if cur==0:
            break
    
    if carry:
        prev.next=Node(carry)

    head=reverse(head)

    return head

def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")

head=add(head)
display(head)