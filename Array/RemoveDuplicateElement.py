def duplicateremove(n):
    s=set()
    for i in n:
        s.add(i)
    return s

n=[1,1,1,1,2]
print(duplicateremove(n))