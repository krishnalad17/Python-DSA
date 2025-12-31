def  nextgreater(n):
    stack=[]
    res=[-1]*len(n)
    for i in range(len(n)):
        while stack and  n[i]>n[stack[-1]]:
            idx=stack.pop()
            res[idx]=n[i]
        stack.append(i)
    return res

print(nextgreater(n=[4,5,2,25]))
