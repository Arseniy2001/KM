# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 1 0 -12 -16 0
# 2 -13 1 103 -183 90
# -2 -13 -13 28
# 0 0 5 -16 -45 0
# six.PY3
from __future__ import print_function
print("Введите полином")
p=list(map(int, raw_input().split()))

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
                elif(p[0]==0 and p[1]==0 and i==2):
                    print(p[i], "x^", (len(p) - 1 - i),sep="", end="")
                elif(p[0]==0 and i==1):
                    print(p[i], "x^", (len(p) - 1 - i),sep="", end="")
                elif(p[0]==0 and p[1]==0 and p[2]==0 and i==3):
                    print(p[i], "x^", (len(p) - 1 - i),sep="", end="")
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
#Умножение полинома на минус если у нас пырвый коэф равен нулю
m=0
n=1
z=0
for i in range(len(p)):
    if z==1:
        p[i]=-1*p[i]
    else:
        if(p[i]!=0 or n==0):
            n=0
            if(i==m and p[i]<0):
                p[i]=-1*p[i]
                z=1
        else:
            m+=1

# Верхняя граница
k=int(0)
s=int(0)
b=(len(p)-1)*[0]
while(k!=1):
    s+=1
    # перебираем числа, пока все его коэфы не больше нуля
    k=1
    n=1
    m=0
    for i in range(len(p) - 1):
        if(p[i]!=0 or n==0):
            n=0
            if(i==m):
                b[i]=p[i]
            else:
                #По схеме горнора вычисляем коэфы
                b[i]=p[i] + b[i - 1]*s
            if(b[i]<0):
                k=-1
            #Если есть коэф<0, то продолжаем перебирать
        else:
            m+=1
f=s

#Для нахождения нижней границы мы должны преобразовать наш полином
for i in range(len(p)):
    if ((len(p) - 1-i)%2==0 and i!=(len(p) - 1)):
        p[i]=-1*p[i]
#Дальше находим верхнюю границу полученного полинома
m=0
n=1
z=0
for i in range(len(p)):
    if z==1:
        p[i]=-1*p[i]
    else:
        if(p[i]!=0 or n==0):
            n=0
            if(i==m and p[i]<0):
                p[i]=-1*p[i]
                z=1
        else:
            m+=1
#Умножение полинома на минус если у нас пырвый коэф равен нулю
k=int(0)
s=int(0)
r=(len(p)-1)*[0]
while(k!=1):
    s+=1
    k=1
    n=1
    m=0
    for i in range(len(p) - 1):
        if(p[i]!=0 or n==0):
            n=0
            if(i==m):
                r[i]=p[i]
            else:
                r[i]=p[i] + r[i - 1]*s
            if(r[i]<0):
                k=-1
        else:
            m+=1
print("Степень полинома:",len(p)-1-m)
print("Нижняя граница:",-1*s)
print("Верхняя граница:", f)

