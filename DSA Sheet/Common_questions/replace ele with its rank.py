# external list sort() apply
def rankorder(l):
    k = l[:]
    k.sort()
    for i in range(len(k)):
        l[l.index(k[i])] = i+1
    return l
def rankDict(l):
    d = { x : y for y,x in enumerate(sorted(l))}
    # or 
    # d = { x : y for y,x in enumerate(l)}
    # sorted_indes = sorted(range(len(l), key = lambda x : l[x]))
    for i in l:
        l[i] = d[l[i]]
    return l
#input
l = list(map(int,input().split()))
print(rankorder(l))