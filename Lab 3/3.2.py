# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 1 1.4 -13.85 1.842 6.264
#
# -1 -2 -2 -5 0 -3 -4 2 -5 0
# 1 4 1 -14 -20 -8
import math
def nul(p):
    p1=[]
    fl1=0
    j=0
    k=0
    while fl1==0:
        if p[j]==0:
            k+=1
        else:
            fl1=1
        j+=1
    for i in range(len(p)-k):
        p1.append(p[i+k])
    return(p1)


print("Введите полином")
p1=list(map(float, raw_input().split()))
p=nul(p1)
if p[0]<0:
    for i in range(len(p)):
        p[i]=-p[i]
fl=0
max=0
for i in range(len(p)):
    if p[i]<0 and fl==0:
        k=i
        fl=1
    if p[i]<0 and abs(p[i])>max:
        max=abs(p[i])

R=1+(max/p[0])**(1./k)
print(max)
print(k)
print(R)