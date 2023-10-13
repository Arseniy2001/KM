# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 1 0 0 -4 1
# 1 3 0 -1
# 1 2 -5 8 -7 -3
# 1 -4 -42 104 361 -420
# -1 -2 -2 -5 0 -3 -4 2 -5 0
# 1 1.4 -13.85 1.842 6.264
# 1 0 1
import math
def nul(p):
    p1=[]
    fl1=0
    j=0
    k=0
    while fl1==0 and j<len(p):
        if p[j]==0:
            k+=1
        else:
            fl1=1
        j+=1
    for i in range(len(p)-k):
        p1.append(p[i+k])
    return(p1)
def Del(b,c):
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
    # print("Частное")
    for i in range(len(a)-len(c)+1):
        Ch.append(a[i])
    # print(Ch)
    # print("Остаток")
    for i in range(len(a)-len(c)+1,len(a)):
        Ost.append(a[i])
    # print(Ost)
    return(Ost)
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
def FUN(b):
    # счетчики изменения знаков
    # k0=0
    k1=0
    k2=0
    ak1=0
    bk1=0
    ak2=0
    bk2=0

    inf=10000
    c=[]
    c=dif(b)

    # # проверяем на знак
    # if fun1(c,0)>0:
    #     print("+")
    # else:
    #     print("-")

    # проверяем на знак
    if fun1(c,inf)>0:
        ak1=1
    else:
        ak1=-1


    # проверяем на знак
    if fun1(b,-inf)>0:
        ak2=1
    else:
        ak2=-1


    while c!=[]:
        d=[]
        for i in range(len(c)):
            d.append(c[i])

        # # проверяем на знак
        # if fun1(c,0)>0:
        #     print("+")
        # else:
        #     print("-")

        # проверяем на знак
        if fun1(c,inf)>0:
            bk1=1
        else:
            bk1=-1
        if ak1*bk1<0:
            k1+=1
        ak1=bk1
        bk1=0

        # проверяем на знак
        if fun1(c,-inf)>0:
            bk2=1
        else:
            bk2=-1
        if ak2*bk2<0:
            k2+=1
        ak2=bk2
        bk2=0
        # с становится равен остатку от деления б на с
        c=Del(b,c)

        # б становится равен с
        b=[]
        for i in range(len(d)):
            b.append(d[i])

        # меняем знак на протвоположный
        for i in range(len(c)):
            c[i]=-c[i]
        c=nul(c)
        # print(c)
    # print(k1,k2)
    return(abs(k1-k2))
print("Введите полином b")
b2=list(map(float, raw_input().split()))
b=nul(b2)
print(FUN(b))

