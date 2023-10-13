# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 1 0 0 -1    1 1 1
# 3 5 0 2 4      1 2 1
# -1 -2 -2 -5 0 -3 -4 2 -5 0
# 1 4 1 -14 -20 -8      1 3
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



print("Введите полином b")
b2=list(map(float, raw_input().split()))
print("Введите полином c")
c2=list(map(float, raw_input().split()))
b=nul(b2)
c=nul(c2)
c1=[]
for i in range(len(c)-1):
    if (abs(c[0]) != 1):
        c1.append(c[len(c)-i-1]/abs(c[0]))
    else:
        c1.append(c[len(c)-i-1])
if c[0]>0:
    for i in range(len(c1)):
        c1[i]=-c1[i]
a=[]
for i in range(len(b)):
    a.append((b[i]))
    for j in range(len(c1)):
        if i<=len(c1)-j-1:
            a[i]=a[i]
        elif j>len(b)-i-1:
            a[i]=a[i]
        else:
            a[i]=a[i]+c1[j]*a[i-len(c1)+j]
Ch=[]
Ost=[]
print("Частное")
for i in range(len(a)-len(c)+1):
    Ch.append(a[i])
print(Ch)
print("Остаток")
for i in range(len(a)-len(c)+1,len(a)):
    Ost.append(a[i])
print(Ost)