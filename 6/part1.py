#!/usr/bin/env python3



def test(s,n):
    for i in range(len(s)-n):
        a = s[i:(i+n)]
        b = s[i+n]
        l = set([a.count(item) for item in a])
        if ((l=={1}) and (b not in a)):
            return i+n+1


with open("input") as f:
    input = f.read()
    print(test(input,3))
    print(test(input,13))

f.close()

