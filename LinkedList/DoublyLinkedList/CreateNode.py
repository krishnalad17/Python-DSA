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

def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")

display(head)