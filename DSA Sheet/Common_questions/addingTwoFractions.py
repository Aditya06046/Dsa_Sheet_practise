# adding or substracting two fractions4
def addFractions(n1,n2,d1,d2):
    n = n1 + n2
    d = float('.'+str(d1)) + float('.'+str(d2))
    print(d)
    return float(n + d)

#input
n1,d1 = map(int,input().split())
n2,d2 = map(int,input().split())
print(addFractions(n1,n2,d1,d2))