#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 1 -8 5 2 -7
# 1 -3 -12 52 -48
# 1 13 57 83 -34 -120 0
# six.PY3
from __future__ import print_function
print("Введите коэффициенты")
p=list(map(int, raw_input().split()))
print("Введите число a")
a=int(input())
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
print("P(x)=", end="")
fun(*p)
print("")

coef=len(p)-1

p2 = []
for j in range(len(p)):
    b = [p[0]]
    for i in range(len(p) - 1):
        b.append(a * b[i] + p[i+1])
    p2.append(b[-1])
    p = b[0:len(b)-1]

p2.reverse()

def fun2(*p):
    for i in range(len(p)):
        if(p[i]>0):
            if (i==0):
                if(p[i]==1):
                    print("y^", (len(p) - 1 - i),sep="", end="")
                else:
                    print( p[i], "y^", (len(p) - 1 - i),sep="", end="")
            else:
                if(p[i]==1):
                    if(i == len(p)-1):
                        print("+", p[i],sep="", end ="")
                    elif(i == len(p) - 2):
                        print("+","y",sep="", end="")
                    else:
                        print("+","y^", (len(p) - 1 - i),sep="", end="")
                else:
                    if(i == len(p)-1):
                        print("+", p[i],sep="", end ="")
                    elif(i == len(p) - 2):
                        print("+", p[i], "y",sep="", end="")
                    else:
                        print("+", p[i], "y^", (len(p) - 1 - i),sep="", end="")
        elif(p[i] == 0):
            print("",sep="", end = "")
        else:
            if(p[i]==-1):
                if(i == len(p)-1):
                    print("", p[i],sep="", end ="")
                elif(i == len(p) - 2):
                    print("","-y",sep="", end="")
                else:
                    print("","-y^", (len(p) - 1 - i),sep="", end="")
            else:
                if(i == len(p)-1):
                    print("", p[i],sep="", end ="")
                elif(i == len(p) - 2):
                    print("", p[i], "y",sep="", end="")
                else:
                    print("", p[i], "y^", (len(p) - 1 - i),sep="", end="")

print("Q(y)=",sep="",end="")
fun(*p2)
print("")
print("Ответ:", p2)