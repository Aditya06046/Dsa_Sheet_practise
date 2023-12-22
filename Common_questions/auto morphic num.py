# if a square of a nubmer ends with same number 25 --> 625
def automorp(n):
    s1 = str(n)
    s2 = str(n*n)
    return s2.endswith(s1)

n = int(input())
print(automorp(n)) 