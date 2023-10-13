# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 1 1.4 -13.85 1.842 6.264
# 1 -4 -42 104 361 -420
# -1 -2 -2 -5 0 -3 -4 2 -5 0
import math

print("Введите полином")
p=list(map(float, raw_input().split()))
maxA=0
maxB=0
fl1=0
j=0
k=0
while fl1==0:
    if p[j]==0:
        k+=1
    else:
        fl1=1
    j+=1
t=0
fl1=0
j=len(p)-1
while fl1==0:
    if p[j]==0:
        t+=1
    else:
        fl1=1
    j-=1
p1=[]
for i in range(len(p)-k-t):
    p1.append(p[i+k])

for i in range(1,len(p1)):
    if abs(p1[i])>maxA:
        maxA=abs(p1[i])
for i in range(len(p1)-1):
    if abs(p1[i])>maxB:
        maxB=abs(p1[i])


R=1+maxA/abs(p1[0])
r=1/(1+maxB/abs(p1[len(p1)-1]))
print(round(R,5),round(r,5))

for i in range(t):
    p1.append(0)
