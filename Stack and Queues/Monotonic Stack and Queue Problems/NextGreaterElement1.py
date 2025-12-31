def nextgreater1(n):
    res=[-1]*len(n)
    for i in range(len(n)):
        for j in range(1,len(n)):
            next=(i+j)%len(n)
            if n[i]<n[next]:
                res[i]=n[next]
                break  
    return res


print(nextgreater1(n=[5,7,1,7,6,0]))