# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 4 0 -95 75 226 -120
# 1 3 -14 -30 49 27 -36
#
# six.PY3
import tkinter as tk
import math

def dif(pol):
    pd = []
    for i in range((len(pol) - 1)):
        pd.append((len(pol) - 1 - i) * pol[i])
    return pd
def print_power(m):
    if m == 2:
        return '\U000000B2'
    elif m == 3:
        return '\U000000B3'
    elif m == 4:
        return '\U00002074'
    elif m == 5:
        return '\U00002075'
    elif m == 6:
        return '\U00002076'
    elif m == 7:
        return '\U00002077'
    elif m == 8:
        return '\U00002078'
    elif m == 9:
        return '\U00002079'
def printp(a):
    pol = ''
    for i in range(len(a)):
        if ((a[i] * 10) % 10) == 0:
            a[i] = int(a[i])
    k = 0
    f = 0
    for i in range(len(a)):
        if a[i] == 0 and f == 0:
            k += 1
        else:
            f = 1
    if len(a)==k:
        pol +='0'
    for i in range(len(a)):
        if a[i] > 0:
            if a[i] == 1:
                if i == k:
                    if i == len(a) - 1:
                        pol += str(a[i])
                    elif i == len(a) - 2:
                        pol += "x"
                    else:
                        pol += "x" + print_power((len(a) - 1 - i))
                else:
                    if i == len(a) - 1:
                        pol += "+" + str(a[i])
                    elif i == len(a) - 2:
                        pol += "+" + "x"
                    else:
                        pol += "+" + "x" + print_power((len(a) - 1 - i))

            else:
                if i == k:
                    if i == len(a) - 1:
                        pol += str(a[i])
                    elif i == len(a) - 2:
                        pol += str(a[i]) + "x"
                    else:
                        pol += str(a[i]) + "x" + print_power((len(a) - 1 - i))
                else:
                    if i == len(a) - 1:
                        pol += "+" + str(a[i])
                    elif i == len(a) - 2:
                        pol += "+" + str(a[i]) + "x"
                    else:
                        pol += "+" + str(a[i]) + "x" + print_power((len(a) - 1 - i))
        elif a[i] == 0:
            pol += ""
        else:
            if a[i] == -1:
                if i == len(a) - 1:
                    pol += "" + str(a[i])
                elif i == len(a) - 2:
                    pol +="-x"
                else:
                    pol +="-x" + print_power((len(a) - 1 - i))
            else:
                if i == len(a) - 1:
                    pol +=str(a[i])
                elif i == len(a) - 2:
                    pol +=str(a[i]) + "x"
                else:
                    pol +=str(a[i]) + "x" + print_power((len(a) - 1 - i))
    return pol
def fun1(p,x):
    b=0
    k=len(p)-1
    for i in range(len(p)):
        b += p[i]*pow(x, k)
        k-= 1
    return b
# нахождение верхней и нижней границы
def maxmin(p):
    v=(len(p))*[0]
    for i in range(len(p)):
        v[i]=p[i]
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
    k=int(0)
    s=int(0)
    b=(len(p)-1)*[0]
    while(k!=1):
        s+=1
        k=1
        n=1
        m=0
        for i in range(len(p) - 1):
            if(p[i]!=0 or n==0):
                n=0
                if(i==m):
                    b[i]=p[i]
                else:
                    b[i]=p[i] + b[i - 1]*s
                if(b[i]<0):
                    k=-1
            else:
                m+=1
    f=s

    for i in range(len(p)):
        if ((len(p) - 1-i)%2==0 and i!=(len(p) - 1)):
            p[i]=-1*p[i]
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

    return s,f

# Метод половинного деления
def Fun(a1,b1,p):
    e=float(0.001)
    if fun1(p, b1)!=0 and fun1(p, a1)!=0:
        c = (a1 + b1) / 2
        while math.fabs(fun1(p,c)) >= e:
            c = (a1 + b1) / 2
            if fun1(p,a1)*fun1(p,c) < 0:
                b1=c
            else:
                a1=c
        a1=(a1 + b1) / 2
    else:
        if fun1(p, b1)==0:
            a1=b1
    return a1

def root(p):
    p1= list(map(float, p))
    mm=maxmin(p1)
    low=float(-1*mm[0])
    up=float(mm[1])
    up=up+0.5
    X=[]
    g=0
    i=0
    while(up-g>=low):
        if fun1(p, up)*fun1(p, up - g)<=0:
            # print(up, up-g)
            if(fun1(p, up)!=0):

                X.append(round(Fun(up,up-g,p),2))

                i+=1
                up=up-g
                g=0
            up=up-g
            g=0
        g+=0.5
    for i in range(len(X)):
        if fun1(p,X[i]+0.5)*fun1(p, X[i]-0.5)>0:
            X.append(X[i])
    X=sorted(X)
    return X

def buttonevent():
    print("Введите полином")
    p = [float(a) for a in coefinput.get().split()]
    X=root(p)

    Res['text']=str(X)
    polinom['text']=printp(X)
def clear():
    polinom['text']=''
    Res['text']=''

window = tk.Tk()
window.geometry('650x250+400+200')
window.title('Частные производные полинома от двух переменных')

tk.Label(text="Введите коэффиценты:").grid(row=0, column=0, sticky='w', padx=10, pady=5)
coefinput = tk.Entry(width=25)
coefinput.grid(row=0, column=1, sticky='w',columnspan=2, padx=10, pady=5)

tk.Label(text="Полином:").grid(row=1, column=0, sticky='w', padx=10, pady=2)
polinom = tk.Label()
polinom.grid(row=1, column=1, sticky='w',columnspan=3, padx=10, pady=2)

tk.Label(text="Ответ").grid(row=2, column=0, sticky='e', padx=10, pady=2)
Res=tk.Label()
Res.grid(row=2, column=1, sticky='w',columnspan=1, padx=10, pady=2)



tk.Button(text="Вычислить", command=buttonevent).grid(row=8, column=1, sticky='w', padx=10, pady=2)

tk.Button(text='Очистить', command=clear,fg='#787878').grid(row=8, column=2, sticky='w', padx=10, pady=2)
tk.mainloop()
