def leader(n):
    res=[]
    for i in range(len(n)):
        leader=True
        for j in range(i+1,len(n)):
            if n[i]<=n[j]:
                leader=False
                break
        if leader:
            res.append(n[i])
    return res



print(leader(n=[4, 7, 1, 0]))