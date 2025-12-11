def rearrage(n):
    neg=1
    pos=0
    res=[0]*len(n)
    for i in range(len(n)):
        if n[i]<0:
           res[neg]=n[i]
           neg+=2
        else :
            res[pos]=n[i]
            pos+=2
    return res

print(rearrage(n=[1,2,3,-1,-2,-3]))