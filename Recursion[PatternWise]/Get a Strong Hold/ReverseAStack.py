def insert_at_bottom(stack,element):
    if not stack:
        stack.append(element)
        return
    temp=stack.pop()
    insert_at_bottom(stack,element)
    stack.append(temp)

def stack_reverse(stack):
    if not stack:
        return
    temp=stack.pop()
    stack_reverse(stack)
    insert_at_bottom(stack,temp)

    
stack=[3,1,2,4]
stack_reverse(stack)
print(stack)

