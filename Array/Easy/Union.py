def union(m,n):
    s=set()
    for i in m:
        s.add(i)
    for i in n:
        s.add(i)
    s=list(s)
    return s

def unionwithlists(m,n):
        res=[]
        for i in m+n:
             if i not in res:
                  res.append(i)
        return res



print(unionwithlists(m=[1,2,3],n=[1,2]))