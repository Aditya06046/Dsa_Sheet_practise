# leap year // 400 or // 4 and !/ 100
def leapyear(n):
    if n % 400 ==0:
        return 1
    elif n % 4 ==0  and n % 100 != 0:
        return 1
    else:
        return 0

#input 
n = int(input())
print(leapyear(n))