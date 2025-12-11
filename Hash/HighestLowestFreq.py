from collections import defaultdict

def frequency(n):
    frq=defaultdict(int)
    maximum=0
    minimum=len(n)
    maxelement=0
    minelement=0
    for i in range(len(n)):
        frq[n[i]]+=1

    for key,value in frq.items():
        if value>maximum:
            maxelement=key
            maximum=value
        if value<minimum:
            minimum=value
            minelement=key
    print(maxelement,maximum)
    print(minelement,minimum)

frequency(n=[1,2,3,1,2,1])
