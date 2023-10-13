# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 1 1.4 -13.85 1.842 6.264
#
# -1 -2 -2 -5 0 -3 -4 2 -5 0
# 1 4 1 -14 -20 -8
import math

def dif(pol):
    pd = []
    for i in range((len(pol) - 1)):
        pd.append((len(pol) - 1 - i) * pol[i])
    return pd
def fun1(p,x):
    b=0
    k=len(p)-1
    for i in range(len(p)):
        b += p[i]*pow(x, k)
        k-= 1
    return(b)

print("Введите полином")
p1=list(map(float, raw_input().split()))
if p1[0]<0:
    for i in range(len(p1)):
        p1[i]=-p1[i]
c=1
p1=dif(p1)
while p1!=[]:
    if fun1(p1,c)>0:
        p1=dif(p1)
    else:
        c+=1
print(c)
