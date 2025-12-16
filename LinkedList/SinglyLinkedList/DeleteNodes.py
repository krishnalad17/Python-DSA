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


def deletefirst(head):
    if head is None:
        return None
    return head.next

def deletelast(head):
    temp=head
    while temp.next.next:
        temp=temp.next 
    temp.next=None
    return head

def deleteatposition(head,p):
    if head is None:
        return None
    if head==1:
        return head.next 
    
    temp=head
    count=1
    while temp.next and count<p-1:
        temp=temp.next 
        count+=1

    temp.next=temp.next.next 
    return head   

def deleteall(head):
    head=None
    return head 

def display(head):
    temp=head
    while temp:
        print(temp.data,end=" -> ")
        temp=temp.next
    print("None")

head=deletefirst(head)
head=deleteatposition(head,3)
head=deletelast(head)
display(head)