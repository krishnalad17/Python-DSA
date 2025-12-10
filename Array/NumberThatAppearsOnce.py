def appearsonce(n):
    for i in range(len(n)):
        count=0
        num=n[i]
        for j in range(len(n)):
            if n[j]==num:
                count+=1
        if count==1:
            return print(num)

def appearsonce1(n):
    xor=0
    for i in n:
        xor ^=i
    return print(xor)


appearsonce1(n=[2,2,1,4,1])