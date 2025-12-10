def sort(n):
    zero=0
    one=0
    two=0

    for i in n:
        if i==0:
            zero+=1
        if i==1:
            one+=1
        if i==2:
            two+=1
    index=0
    for i in range(zero):
        n[index]=0
        index+=1

    for i in range(one):
        n[index]=1
        index+=1

    for i in range(two):
        n[index]=2
        index+=1
        
    return n

print(sort(n=[0,1,0,1,2,2,0,1]))