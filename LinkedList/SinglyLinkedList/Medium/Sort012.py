class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(0)
b=Node(1)
c=Node(2)
d=Node(0)

a.next=b
b.next=c
c.next=d

head=a

def sort(head):
    if head is None or head.next is None:
        return head
    cur=head
    
    zerod=Node(0)
    oned=Node(0)
    twod=Node(0)

    zero=zerod
    one=oned
    two=twod


    while cur:
        if cur.data==0:
            zero.next=cur
            zero=zero.next
        elif cur.data==1:
            one.next=cur
            one=one.next
        else:
            two.next=cur
            two=two.next
        cur=cur.next 

    two.next=None
    zero.next=oned.next if oned.next else twod.next
    one.next=twod.next 

    return zerod.next


def display(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("None")

head=sort(head)
display(head)
