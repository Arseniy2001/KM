#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -5 -1 3 -2 5
# -3 -2 0 -2 1 1.3
# -0.9 2.1 3.7 -2.4 0.8 3
# six.PY3
from __future__ import print_function
print("Введите коэффициенты")
a=list(map(float, raw_input().split()))
coef=len(a)-1
print("Введите число")
x=float(input())
b=0
for i in range(len(a)):
    b += a[i]*pow(x, coef)
    coef -= 1

for i in range(len(a)):
    if (((a[i]*10)%10)==0):
        a[i]=int(a[i])
print("F(x)=",sep="",end="")
for i in range(len(a)):
    if(a[i]>0):
        if(a[i]==1):
            if(i == len(a)-1):
                print("+",a[i],sep="", end = "")
            elif(i==len(a)-2):
                print("+","x",sep="", end="")
            else:
                print("+","x^",(len(a) - 1 - i),sep="", end="")
        else:
            if(i == len(a)-1):
                print("+",a[i],sep="", end = "")
            elif(i==len(a)-2):
                print("+",a[i],"x",sep="", end="")
            else:
                print("+",a[i],"x^",(len(a) - 1 - i),sep="", end="")
    elif(a[i]==0):
        print("",sep="", end = "")
    else:
        if(a[i]==-1):
            if(i == len(a)-1):
                print("",a[i],sep="", end = "")
            elif(i==len(a)-2):
                print("","x",sep="", end="")
            else:
                print("","x^",(len(a) - 1 - i),sep="", end="")
        else:
            if(i == len(a)-1):
                print("",a[i],sep="", end = "")
            elif(i==len(a)-2):
                print("",a[i],"x",sep="", end="")
            else:
                print("",a[i],"x^",(len(a) - 1 - i),sep="", end="")
print("")
if (b*10)%10==0:
    b=int(b)
    print ("Ответ:F(",int(x),")=",b,sep="")
else:
    print("Ответ: F(",x,")=",round(b,3),sep="")
print("Степень полинома:",len(a)-1)
