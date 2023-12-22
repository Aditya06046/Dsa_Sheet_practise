def Greatest_among_threee(a,b,c):
    return  a if (a>b and a>c) else (b if b>c else c )
### use max(a,b,c)
# using ternary operator in c
# val = a>b ?  a>c ? a: c : b>c ? b : c 

a ,b ,c  = map(int,input().split())
print(Greatest_among_threee(a,b,c))
print(max(a,b,c))
