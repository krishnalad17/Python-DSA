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

def deletefirst(head):
    if head is None:
        return None
    return head.next
        
def deletelast(head):
    if head is None:
        return None  
    temp=head
    while temp.next.next:
        temp=temp.next 
    temp.next=None
    return head

def deleteatposition(head,k):
    if head is None:
        return None  
    if k==1:
        return head.next 
    temp=head
    count=1
    while temp is not None and count<k-1:
        temp=temp.next 
        count+=1
    temp.next.prev=temp
    temp.next=temp.next.next 
    return head

def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")

head=deletefirst(head)
head=deletelast(head)
head=deleteatposition(head,1)
display(head)