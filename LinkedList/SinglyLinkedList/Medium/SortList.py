class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(10)
b=Node(60)
c=Node(50)
d=Node(40)

a.next=b
b.next=c
c.next=d

head=a

def sortlist(head):
    if  head is None or  head.next is None:
        return head
    
    mid=middle(head)
    right=mid.next 
    mid.next=None

    left=sortlist(head)
    right=sortlist(right)

    return merge(left,right)

def middle(head):
    slow=head
    fast=head
    while fast and fast.next.next:
        fast=fast.next.next 
        slow=slow.next
    return slow

def merge(l1,l2):
    dum=Node(0)
    cur=dum

    while l1 and l2:
        if l1.data <= l2.data:
            cur.next=l1
            l1=l1.next 
        else :
            cur.next=l2
            l2=l2.next 
        cur=cur.next 
    cur.next=l1 if l1 else l2
    return dum.next

    

def display(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("None")

head=sortlist(head)
display(head)
