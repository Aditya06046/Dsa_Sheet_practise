# finding nth fibonacci number
def nthfibo(n):
    x , y = 0 , 1
    if n == 1 :
        return 0
    if n == 2  or n == 3:
        return 1
    else:
        n = n-3
        while n > 0:
            temp = x+y
            x = y 
            y = temp
            n -= 1
        return x+y
    return -1
def fib_series(n):
    if n <= 1:
        return n
    return fib_series(n-1) + fib_series(n-2)
### input
n = int(input())
# print(nthfibo(n))
print(fib_series(n))