def rotation(l,k):
    for _ in range(k):
        l.append(l.pop(0))
    return l

#input
l = list(map(int,input().split()))
k = int(input())
print(rotation(l,k))