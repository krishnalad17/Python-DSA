def leftshift1(n):
    temp=n[0]
    for i in range(1,len(n)):
        n[i-1]=n[i]
    n[-1]=temp
    return n


def leftshift2(n):
    temp=[0]*len(n)
    for i in range(1,len(n)):
        temp[i-1]=n[i]
    temp[-1]=n[0]
    return temp


n=[1,5,1,2,3]
print(leftshift2(n))