# two strings are anagrams if combination of one string == another string
# with using sorted() method O(nlog(n))
# ascii valses A-Z 65-90 a-z 97-122
import time
def anagram(a,b):
    return sorted(a)==sorted(b)

# without using sorted() method O(n) ,O(n) time and space
def Anagram_lesstime(a, b):
    l ={}
    for i in a:
        l[i] = l.get(i,0) + 1
    for i in b:
        if i not in l:
            return False
        l[i] = l[i] - 1
        if l[i] == 0:
            del l[i]
    return not l

# without using any external space O(c)--> constant space
def const_space(a ,b):
    cs = [0] * 26
    for i in a:
        cs[ord(i)-97] += 1
    for i in b:
        cs[ord(i)-97] -=1
    return all( i==0 for i in cs)

#input
s1, s2 = map(str , input().split())
s = time.time()
# print(Anagram_lesstime(s1,s2))
print(const_space(s1,s2))
t = time.time()
print((t-s)*1000)