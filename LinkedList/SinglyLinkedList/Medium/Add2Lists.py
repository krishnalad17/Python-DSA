class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(1)
b=Node(1)
c=Node(1)
d=Node(1)

a.next=b
c.next=d

head1=a
head2=c

def add(head1,head2):
    dum=Node(0)
    temp=dum
    carry=0

    cur1=head1
    cur2=head2

    while cur1 or cur2 or carry:
        total=carry

        if cur1:
            total+=cur1.data
            cur1=cur1.next 
        
        if cur2:
            total+=cur2.data
            cur2=cur2.next
        
        carry=total//10
        temp.next=Node(total%10)
        temp=temp.next 
    return dum.next
    

def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")

head=add(head1,head2)
display(head)