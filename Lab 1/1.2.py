# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 3 1 -8 0 8 7 6    -2
# 8 -7 28 -5 -40 10 -3 -28 -17 -9    1
# 1 -1 -6 4 8     2
# six.PY3
from __future__ import print_function
print("Введите полином")
p=list(map(int, raw_input().split()))
b=[]
print("Введите значение a")
s=int(input())

b.append(p[0])
for i in range(1, len(p) - 1):
    b.append(p[i] + b[i - 1] * s)

def fun(*p):
    for i in range(len(p)):
        if(p[i]>0):
            if (i==0):
                if(p[i]==1):
                    print("x^", (len(p) - 1 - i),sep="", end="")
                else:
                    print( p[i], "x^", (len(p) - 1 - i),sep="", end="")
            else:
                if(p[i]==1):
                    if(i == len(p)-1):
                        print("+", p[i],sep="", end ="")
                    elif(i == len(p) - 2):
                        print("+","x",sep="", end="")
                    else:
                        print("+","x^", (len(p) - 1 - i),sep="", end="")
                else:
                    if(i == len(p)-1):
                        print("+", p[i],sep="", end ="")
                    elif(i == len(p) - 2):
                        print("+", p[i], "x",sep="", end="")
                    else:
                        print("+", p[i], "x^", (len(p) - 1 - i),sep="", end="")
        elif(p[i] == 0):
            print("",sep="", end = "")
        else:
            if(p[i]==-1):
                if(i == len(p)-1):
                    print("", p[i],sep="", end ="")
                elif(i == len(p) - 2):
                    print("","-x",sep="", end="")
                else:
                    print("","-x^", (len(p) - 1 - i),sep="", end="")
            else:
                if(i == len(p)-1):
                    print("", p[i],sep="", end ="")
                elif(i == len(p) - 2):
                    print("", p[i], "x",sep="", end="")
                else:
                    print("", p[i], "x^", (len(p) - 1 - i),sep="", end="")
print("Степень полинома:", len(p)-1)
print("Введенный полином: P(x)=", end="")
fun(*p)
print (" ")
print("После замены: Q(x)=", end="")
fun(*b)
print(" ")
print("Ответ: [", end="")
for i in range(len(b)):
    if i==len(b)-1:
        print(b[i], end=" ")
    else:
        print(b[i],",",sep="", end=" ")
print("]",end="")