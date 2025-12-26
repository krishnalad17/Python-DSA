def frequency(s):
    freq={}
    maxi=0
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    sorted_list=sorted(freq.items(),)
