def leader(n):
    l=len(n)
    lead=n[l-1]
    res=[]
    for i in range (l):
        for j in range(i,l):
            if n[i]>lead and n[i]>n[j]:
                res.append(n[i])
    return set(res)

print(leader(n=[4, 7, 1, 0]))