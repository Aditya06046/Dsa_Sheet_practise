def xorop(l):
    n = max(l)
    s = (n*(n+1))//2
    val = sum(l)
    return s - val

#input
def xoropt(l):
    val =l[0]
    for i in range(1,len(l)):
        val = val ^ l[i]
        print(val)
# l = list(map(int,input().split()))
# print(xoropt(l))
print()