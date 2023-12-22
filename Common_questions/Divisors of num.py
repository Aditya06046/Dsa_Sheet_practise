# if i is a divisor then n/i is also a divisor 0(log(n))
# iterate through sqrt(n)
def Divisor(n):
    val = int(n **(0.5))
    l = [1]
    for i in range(2,val):
        if n % i == 0:
            l.append(i)
            if i != n //i :
                l.append(n//i)
    return l 

# input
n = int(input())
print(Divisor(n))