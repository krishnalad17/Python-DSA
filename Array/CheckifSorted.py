def checksort1(n):
    l=len(n)
    for i in range(l):
        for j in range(i+1,l):
            if n[j]<n[i]:
                return False
    return True

def checksort2(n):
    l=len(n)
    for i in range (1,l):
        if n[i]<n[i-1]:
            return True
    return False


n=[1,1,2,3]
print(checksort2(n))

