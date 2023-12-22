#gcd of two nubmers normal approach 0(min(a,b))
def gcdoftwoNum(a,b):
    m = min(a,b)
    gcd = 1
    for i in range(2,m+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

### #gcd of two nubmers normal approach 0(log(min(a,b)))
def Euclidean_formula_Gcd(a,b):
    while b:
        a , b = b ,a%b
    return a
## with recursion 
def recur_gcd(a,b):
    if a == 0:
        return b
    elif b == 0 :
        return a
    elif a == b:
        return a
    elif a > b :
        return recur_gcd(b ,a-b)
    else :
        return recur_gcd(b-a ,a)
# input
a , b =map(int, input().split())
# print(gcdoftwoNum(a,b))
# print(Euclidean_formula_Gcd(a,b))
print(recur_gcd(a,b))