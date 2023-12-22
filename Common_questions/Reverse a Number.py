# reverse a number with out converting into string 
def reverse_num(n):
    res = 0 
    while n > 0:
        rem = n % 10
        res = res*10 + rem
        n //= 10
    return res

# reverse a number using str() 
def reverse_str(n):
    return str(n)[::-1]
n = int(input())
print(reverse_str(n))