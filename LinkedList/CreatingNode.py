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

temp=head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print("None")