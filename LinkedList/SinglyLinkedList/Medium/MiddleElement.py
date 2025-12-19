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
d.next=None
head=a

def middle(head):
    slow=head
    fast=head

    while fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow.data

print(middle(head))