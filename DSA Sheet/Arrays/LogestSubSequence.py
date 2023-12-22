def LongestSubSequence(l):
    k = []
    for i in l:
        c = 1
        n = 1
        while i+n in l:
            n += 1
            c += 1
        k.append((i,c))
    print(k)
    return max(k , key = lambda x : x[1])

#input
l = list(map(int,input().split()))
print(LongestSubSequence(l))