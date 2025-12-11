from collections import defaultdict

def frequency(n):
    frq=defaultdict(int)

    for i in range(len(n)):
        frq[n[i]]+=1

    for key,value in frq.items():
        print(key,value)

frequency(n=[1,2,3,1,2,3,1])
