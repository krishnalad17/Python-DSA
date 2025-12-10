def zeroend1(n):
    temp=[]*len(n)
    for i in range (len(n)):
        if n[i]!=0:
            temp.append(n[i])
    for i in range(len(temp),len(n)):
        temp.append(0)
    return temp

def zeroend2(n):
    temp=[0]*len(n)
    index=0
    for i in range(len(n)):
        if n[i]!=0:
         temp[index]=n[i]
         index+=1
    for i in range (len(n)):
        n[i]=temp[i]
    return n

n=[0,0,1,2,0,3,0]
print(zeroend2(n))