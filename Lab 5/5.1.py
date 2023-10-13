# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 5 4 ; 3 -2
# 4 -4 0 ; 3 1 3 ; 1 2 -3
# 3 4 -1 -1 ; -1 -3 1 -1 ; -2 -4 4 2 ; -1 0 -5 0
# -6.5 7.8 8.1 ; 1.6 2.4 -9.1 ; -8.1 3.1 -1
# 1 2 3 4 ; 2 1 2 3 ; 3 2 1 2 ; 4 3 2 1
import tkinter as tk
import numpy as np

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
                        pol += "λ"
                    else:
                        pol += "λ" + print_power((len(a) - 1 - i))
                else:
                    if i == len(a) - 1:
                        pol += "+" + str(a[i])
                    elif i == len(a) - 2:
                        pol += "+" + "λ"
                    else:
                        pol += "+" + "λ" + print_power((len(a) - 1 - i))

            else:
                if i == k:
                    if i == len(a) - 1:
                        pol += str(a[i])
                    elif i == len(a) - 2:
                        pol += str(a[i]) + "λ"
                    else:
                        pol += str(a[i]) + "λ" + print_power((len(a) - 1 - i))
                else:
                    if i == len(a) - 1:
                        pol += "+" + str(a[i])
                    elif i == len(a) - 2:
                        pol += "+" + str(a[i]) + "λ"
                    else:
                        pol += "+" + str(a[i]) + "λ" + print_power((len(a) - 1 - i))
        elif a[i] == 0:
            pol += ""
        else:
            if a[i] == -1:
                if i == len(a) - 1:
                    pol += "" + str(a[i])
                elif i == len(a) - 2:
                    pol +="-λ"
                else:
                    pol +="-λ" + print_power((len(a) - 1 - i))
            else:
                if i == len(a) - 1:
                    pol +=str(a[i])
                elif i == len(a) - 2:
                    pol +=str(a[i]) + "λ"
                else:
                    pol +=str(a[i]) + "λ" + print_power((len(a) - 1 - i))
    return pol
# преобразование в матрицу строки
def mat(p):
    mat = []
    for line in p.split(';'):
        mat.append(line.split())
    return np.array(mat).astype(float)
# умножение матриц
def mul(a,b):
    res = np.zeros((len(a), len(b[0])))
    s = 0
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                s += a[i][k]*b[k][j]
            res[i][j]=s
            s=0
    return res
# нахождение следа матрицы
def getS(m1,n):
    k=1
    m2=m1.copy()
    while k!=n:
        k+=1
        m2=mul(m2,m1)
    s=0
    for i in range(len(m2)):
        s+=m2[i,i]
    return(s)
# основная функция вычисления коэффицентов
def MainFun(m):
    p=np.zeros(len(m))
    for i in range(len(m)):
        p[i]=getS(m,i+1)
        for j in range(i):
            p[i]+=p[j]*getS(m,i-j)
        p[i]=p[i]/-(i+1)
    return(p)
def buttonevent():
    p1 = str(coefinput1.get())
    a=mat(p1)
    res=MainFun(a)
    res=np.insert(res,0,1)
    for i in range(len(res)):
        if ((res[i] * 10) % 10) == 0:
            res[i] = int(res[i])
        else:
            res[i] = round(res[i],4)


    Res1['text']=printp(res)
    Res2['text']=res
def clear():
    power['text']=''
    Res1['text']=''
    Res2['text']=''


window = tk.Tk()
window.geometry('+400+200')
window.title('Метод Лаверрье')

tk.Label(text="Введите квадратную матрицу матрицу").grid(row=0, column=0, sticky='w', padx=10, pady=5)
coefinput1 = tk.Entry(width=25)
coefinput1.grid(row=0, column=1, sticky='w',columnspan=2, padx=10, pady=5)

tk.Label(text="Размер матрицы A:").grid(row=2, column=0, sticky='e', padx=10, pady=2)
power = tk.Label()
power.grid(row=2, column=1, sticky='w',columnspan=3, padx=10, pady=2)

tk.Label(text="Коэффиценты полином: ").grid(row=3, column=0, sticky='e', padx=10, pady=2)
Res2=tk.Label()
Res2.grid(row=3, column=1, sticky='w',columnspan=1, padx=10, pady=2)

tk.Label(text="Характеристический полином: ").grid(row=4, column=0, sticky='e', padx=10, pady=2)
Res1=tk.Label()
Res1.grid(row=4, column=1, sticky='w',columnspan=1, padx=10, pady=2)


tk.Button(text="Вычислить", command=buttonevent,fg='#787878').grid(row=8, column=1, sticky='w', padx=10, pady=2)

tk.Button(text='Очистить', command=clear,fg='#787878').grid(row=8, column=2, sticky='w', padx=10, pady=2)
tk.mainloop()