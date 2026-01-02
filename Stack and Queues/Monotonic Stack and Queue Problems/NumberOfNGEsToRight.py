def numberofnges1(n):
    res=[]
    for i in range(len(n)):
        counter=0
        for j in range(i+1,len(n)):
            if n[j]>n[i]:
                counter+=1
        res.append(counter)
    return res

def numberofnges2(n):
    res=[0]*len(n)
    stack=[]

    for i in range(len(n)-1,-1,-1):
        while stack and stack[-1]<=n[i]:
            stack.pop()
        res[i]=len(stack)
        stack.append(n[i])
    return res


print(numberofnges1(n=[3,4,2,7,5]))
