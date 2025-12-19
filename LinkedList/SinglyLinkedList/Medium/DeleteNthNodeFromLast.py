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

def deletenthnode(head,p):
    slow=head
    fast=head
    for i in range(p+1):
        if fast is None:
            return head
        fast=fast.next 
    while fast:
        fast=fast.next 
        slow=slow.next 
    slow.next=slow.next.next 
    return head


def display(head):
    temp=head
    while temp:
        print(temp.data,end=" -> ")
        temp=temp.next
    print("None")

head=deletenthnode(head,2)
display(head)