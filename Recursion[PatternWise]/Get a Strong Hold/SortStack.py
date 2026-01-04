def sort_stack(stack):
    if not stack:
        return

    temp=stack.pop()

    sort_stack(stack)

    insert_sorted(stack,temp)


def insert_sorted(stack,x):
    if not stack or stack[-1]<=x:
        stack.append(x)
        return
    temp=stack.pop()
    insert_sorted(stack,x)

    stack.append(temp)
    
stack=[3,1,2,4]
sort_stack(stack)
print(stack)

