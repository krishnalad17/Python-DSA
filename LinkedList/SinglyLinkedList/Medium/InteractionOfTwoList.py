class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(1)
b=Node(3)
c=Node(1)
d=Node(2)
e=Node(3)
f=Node(4)

a.next=b
b.next=c
c.next=d

head1=a

head2=e

e.next=d
d.next=f

def interaction(head1,head2):
    d1=head1
    d2=head2

    while d1!=d2:
        d1=d1.next 
        d2=d2.next 

        if d1.next is None:
            d1=head2
        if d2.next is None:
            d2=head1
    return d1.data

head=interaction(head1,head2)
print(head)

