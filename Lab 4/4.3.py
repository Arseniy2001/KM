# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 0 0 0 ; 0 0 5 ; -2 4 3
# 1 6 -4 ; -8 6 7 ; -7 0 8
# -4.6 -1.71 -3.06 ; 2.66 -3.52 0.22 ; -0.79 -1.9 -4.04
# 1 0 0 ; 0 1 0 ; 0 0 1

# 1 2 3 ; 4 5 6 ; 7 8 9
import tkinter as tk
import numpy as np

def mat(p):
    mat = []
    for line in p.split(';'):
        mat.append(line.split())
    return np.array(mat).astype(float)
# определение номера элемента равного 1 или элемент не равный 0
def Num(m):
    p=-1
    q=-1
    fl=0
    for j in range(len(m[0])):
        for i in range(len(m)):
            if m[i,j]==1 and fl==0:
                fl=1
                p=i
                q=j
    if fl==0:
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j]!=0 and fl==0:
                    fl=1
                    p=i
                    q=j
    if p==-1 and q==-1:
        p=0
        q=0
        a=m[p][q]
    else:
        a=m[p][q]
    print(p,q,a)
    return(p,q,a)
# нахождение следующего определителя по формуле
def FunDet(m,p,q,a):
    res=np.zeros((len(m)-1,len(m[0])-1))
    # преобразование столбца если нету элемента ==1
    for i in range(len(m)):
        m[i,q]=m[i,q]/a
    print(m)
    print(p,q,a)
    for i in range(len(m)-1):
        for j in range(len(m[0])-1):
            # aij=aij-aip*apj/app
            if i<p and j<q:
                res[i,j]=(m[i,j]-m[i,q]*m[p,j])*pow(-1,p+q+2)
            elif i>=p and j<q:
                res[i,j]=m[i+1,j]-m[i+1,q]*m[p,j]*pow(-1,p+q+2)
            elif i<p and j>=q:
                res[i,j]=m[i,j+1]-m[i,q]*m[p,j+1]*pow(-1,p+q+2)
            else:
                res[i,j]=m[i+1,j+1]-m[i+1,q]*m[p,j+1]*pow(-1,p+q+2)
    print(res)
    for i in range(len(m)-1):
        res[i,0]=res[i,0]*a
    return(res)
def Det(m):
    N=Num(m)
    # 0 - столбец 1 - строка 2 - значение
    p=N[0]
    q=N[1]
    a=N[2]
    # находим опредеоитель на порядок меньше
    Mn=FunDet(m,p,q,a)
    while len(Mn)!=1:
        N=Num(Mn)
        p=N[0]
        q=N[1]
        a=N[2]
        Mn=FunDet(Mn,p,q,a)
    return(Mn)



def buttonevent():
    text=''
    p1 = str(coefinput1.get())
    a=mat(p1)
    res=float(Det(a))
    if ((res * 10) % 10) != 0:
        text=str(round(float(res),3))
    else:
        text=str(round(int(res),3))

    if text=="NaN" or text=="-NaN" or text=="nan" or text=="-nan":
        Res1['text']='0'
    else:
        Res1['text']=text
    i1=len(a)
    j1=len(a[0])
    power['text']=str(i1)+' x '+str(j1)

def clear():
    power['text']=''
    Res1['text']=''


window = tk.Tk()
window.geometry('+400+200')
window.title('Определитель матрицы')

tk.Label(text="Введите матрицу A").grid(row=0, column=0, sticky='w', padx=10, pady=5)
coefinput1 = tk.Entry(width=25)
coefinput1.grid(row=0, column=1, sticky='w',columnspan=2, padx=10, pady=5)

tk.Label(text="Размер матрицы A:").grid(row=2, column=0, sticky='e', padx=10, pady=2)
power = tk.Label()
power.grid(row=2, column=1, sticky='w',columnspan=3, padx=10, pady=2)


tk.Label(text="DetA = ").grid(row=4, column=0, sticky='e', padx=10, pady=2)
Res1=tk.Label()
Res1.grid(row=4, column=1, sticky='w',columnspan=1, padx=10, pady=2)


tk.Button(text="Вычислить", command=buttonevent,fg='#787878').grid(row=8, column=1, sticky='w', padx=10, pady=2)

tk.Button(text='Очистить', command=clear,fg='#787878').grid(row=8, column=2, sticky='w', padx=10, pady=2)
tk.mainloop()