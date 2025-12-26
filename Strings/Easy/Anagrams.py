def anagrams(s,t):
    if len(s)!=len(t):
        return False
    s=sorted(s)
    t=sorted(t)
    for i in range(len(s)):
        if s[i]!=t[i]:
            return False
    return True

def anagrams1(s,t):
    if len(s)!=len(t):
        return False
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch]-=1
        if freq[ch]<0:
            return False
    return True

def isanagram(s,t):
    return sorted(s)==sorted(t)

print(anagrams1(s="cat",t="act"))