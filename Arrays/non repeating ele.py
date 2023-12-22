def nonrep(l):
    d = {}
    for i in l:
        d[i] = d.get(i,0) + 1
    return [i for i,j in d.items() if j==1]

l = list(map(int,input().split()))
print(nonrep(l))