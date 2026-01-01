def nextgreater1(n):
    res=[-1]*len(n)
    for i in range(len(n)):
        for j in range(1,len(n)):
            next=(i+j)%len(n)
            if n[i]<n[next]:
                res[i]=n[next]
                break  
    return res

def nextgreater2(n):
    ans=[0]*len(n)
    stack=[]

    for i in range(2*len(n)-1,-1,-1):
        cur=n[i % len(n)]

        while stack and stack[-1]<=cur:
            stack.pop()
        
        if i<len(n):
            if stack:
                ans[i]=stack[-1]

        stack.append(cur)
    return ans


print(nextgreater2(n=[5,7,1,7,6,0]))