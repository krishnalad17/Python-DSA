class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(1)
b=Node(2)
c=Node(3)

a.next=b
b.next=c
head=a

def seggregate(head):
    ehead=None
    etail=None
    ohead=None
    otail=None
    cur=head

    while cur:
        if cur.data%2==0:
            if ehead is None:
                ehead=cur
                etail=cur
            else:
                etail.next=cur
                etail=etail.next 
        else:
            if ohead is None:
                ohead=cur
                otail=cur
            else:
                otail.next=cur
                otail=otail.next 
        cur=cur.next 
    if etail:
        etail.next=ohead
        return ehead
    return ohead       

def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")

head=seggregate(head)
display(head)