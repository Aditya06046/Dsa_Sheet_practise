# frequency of unique items in the list
# two ways Counter module and Dictionary
from collections import Counter
def Counter_ele(l):
    l = Counter(l)
    k = []
    for i, j in l.items():
        k.append((i,j))
    return k
def DictCount(l):
    d ={}
    for i in l:
        d[i] = d.get(i, 0)+1
    # sorting dict based on the keys , values
    d1 = sorted(d) # sorted order of keys as list
    d = dict(sorted(d.items() , key = lambda x : x[0], reverse = False)) # sorted dict based on the values x[1] if x[0] on vales
    return d

#input
l = list(map(int,input().split()))
print(DictCount(l))