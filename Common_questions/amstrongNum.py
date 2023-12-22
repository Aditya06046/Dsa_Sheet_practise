import math
def amstrong(n):
    x =int(math.log(n,10))+1
    s = 0
    for i in str(n):
        s +=int(i)**x
    print(s)
    return s == n
#input
n = int(input())
print(amstrong(n))