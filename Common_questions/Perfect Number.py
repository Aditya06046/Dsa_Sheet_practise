# perfect num is sum of its divisors except the given nubmer is equals to original nubmer 
def Divisor(n):
    val = int(n **(0.5))
    l = [1]
    for i in range(2,val):
        if n % i == 0:
            l.append(i)
            if i != n //i :
                l.append(n//i)
    return l 
def perfect_Number(n):
    val = sum(Divisor(n))
    if val == n:
        return 1
    return 0
# or 
def combine_pro(n):
    val = int(n **(0.5))
    l = 1
    for i in range(2,val):
        if n % i == 0:
            l += i
            if i != n //i :
                l += n//i
    return l == n 
# input
n = int(input())
print(combine_pro(n))