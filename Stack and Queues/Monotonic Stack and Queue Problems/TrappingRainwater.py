def traprainwater(n):
    if len(n)==0:
        return 0
    
    leftmax=[0]*len(n)
    rightmax=[0]*len(n)
    for i in range(1,len(n)):
        leftmax[i]=max(leftmax[i-1],n[i])
    for i in range(len(n)-2,-1,-1):
        rightmax[i]=max(rightmax[i+1],n[i])
    water=0
    for i in range(len(n)):
        water+=min(leftmax[i],rightmax[i])-n[i]
    return water

print(traprainwater(n=[0,1,0,2,1,0,1,3,2,1,2,1]))
