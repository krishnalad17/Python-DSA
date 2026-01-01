def nextsmaller(n):
    ans=[-1]*len(n)
    stack=[]

    for i in range(len(n)):
        while stack and n[stack[-1]]>=n[i]:
            idx=stack.pop()
            ans[idx]=n[i]
        stack.append(i)
    return ans

print(nextsmaller(n=[4,5,2,25]))
