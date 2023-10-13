# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk


# 4 3 0 −3 ; 1 1 3 −4
# 2 0 ; 1 0      1 -3 ; 4 -2
# 0 -1 2 ; 1 0 3 ; 4 -3 -2      1 0 0 ; 0 1 0 ; 0 0 1
# 7 7 3 ; -2 -4 1 ; 2 7 -7       7 7 3 ; -2 -4 1 ; 2 7 -7
import math
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


def mat(p):
    mat = []
    for line in p.split(';'):
        mat.append(line.split())
    return np.array(mat).astype(float)
# Умножение матриц размером <2х2
def mul(a,b):
    res = np.zeros((len(a), len(b[0])))
    s = 0
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                s += a[i, k] * b[k, j]
            res[i, j] = s
            s = 0
    return res
# рекурсивное разбиение матриц на 4 блока
def mulblock(a,b):
    if (len(a[0])==len(b)) and (a.shape == (2, 2) or a.shape == (1, 1) or a.shape == (1, 2) or a.shape == (2, 1)):
        res=mul(a,b)
        return(res)
    else:
        res1=mulblock(a[0:len(a) // 2, 0:len(a[0]) // 2],b[0:len(b) // 2, 0:len(b[0]) // 2])+ mulblock(a[0:len(a) // 2, len(a[0]) // 2:], b[len(b) // 2:, 0:len(b[0]) // 2])
        res2 = mulblock(a[0:len(a) // 2, 0:len(a[0]) // 2],b[0:len(b) // 2, len(b[0]) // 2:]) + mulblock(a[0:len(a) // 2, len(a[0]) // 2:], b[len(b) // 2:, len(b[0]) // 2:])
        res3 = mulblock(a[len(a) // 2:, 0:len(a[0]) // 2], b[0:len(b) // 2, 0:len(b[0]) // 2]) + mulblock(a[len(a) // 2:, len(a[0]) // 2:], b[len(b) // 2:, 0:len(b[0]) // 2])
        res4 = mulblock(a[len(a) // 2:, 0:len(a[0]) // 2], b[0:len(b) // 2, len(b[0]) // 2:]) + mulblock(a[len(a) // 2:, len(a[0]) // 2:], b[len(b) // 2:, len(b[0]) // 2:])

        res=np.hstack((np.vstack((res1,res3)),np.vstack((res2,res4))))
    return(res)
def buttonevent():
    p1 = str(coefinput1.get())
    p2 = str(coefinput2.get())
    a=mat(p1)
    b=mat(p2)
    Res1['text']=mul(a,b)
    i=len(a)
    j=len(b)
    power['text']=str(i)+' x '+str(j)
def clear():
    power['text']=''
    Res1['text']=''




window = tk.Tk()
window.geometry('+400+200')
window.title('Умножение квадратных матриц')

tk.Label(text="Введите A").grid(row=0, column=0, sticky='w', padx=10, pady=5)
coefinput1 = tk.Entry(width=25)
coefinput1.grid(row=0, column=1, sticky='w',columnspan=2, padx=10, pady=5)

tk.Label(text="Введите B").grid(row=1, column=0, sticky='w', padx=10, pady=5)
coefinput2 = tk.Entry(width=25)
coefinput2.grid(row=1, column=1, sticky='w',columnspan=2, padx=10, pady=5)



tk.Label(text="Размер матрицы A * B:").grid(row=2, column=0, sticky='e', padx=10, pady=2)
power = tk.Label()
power.grid(row=2, column=1, sticky='w',columnspan=3, padx=10, pady=2)


tk.Label(text="A * B = ").grid(row=4, column=0, sticky='e', padx=10, pady=2)
Res1=tk.Label()
Res1.grid(row=4, column=1, sticky='w',columnspan=1, padx=10, pady=2)


tk.Button(text="Вычислить", command=buttonevent,fg='#787878').grid(row=8, column=1, sticky='w', padx=10, pady=2)

tk.Button(text='Очистить', command=clear,fg='#787878').grid(row=8, column=2, sticky='w', padx=10, pady=2)
tk.mainloop()