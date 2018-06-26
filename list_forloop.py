#!/usr/bin/python

l1 = [6,1,2,8,10]
l2 = [2,3,1,5,20,30,10]

for a,b in zip(l1,l2):
    if a>b:
        print(a)
    else:
        print(b)