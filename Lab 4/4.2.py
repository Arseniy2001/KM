# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 1 4 1 3 ; 0 -1 3 -1 ; 3 1 0 2 ; 1 -2 5 1
# 1 -2 ; 3 -2
# 1 0 0 ; 0 1 0 ; 0 0 1
# 1 6 -4 ; -8 6 7 ; -7 0 8
# 1 2 3 ; 4 5 6 ; 7 8 9
import tkinter as tk
import numpy as np

def mat(p):
    mat = []
    for line in p.split(';'):
        mat.append(line.split())
    return np.array(mat).astype(float)
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

# обратная матрица 2 на 2 или 1 на 1
def invMat(m):
    res=np.zeros((len(m),len(m[0])))
    if len(m)==2:
        delta=m[0][0]*m[1][1]-m[0][1]*m[1][0]
        if delta==0:
            return([[0]])
        else:
            for i in range(len(m)):
                for j in range(len(m[0])):
                    if (i==0 and j==1) or (i==1 and j==0):
                        res[i][j]=-m[i][j]/delta
                    else:
                        res[i][j]=m[len(m)-1-i][len(m[0])-1-j]/delta

    else:
        if m[0][0]==0:
            return([[m[0][0]]])
        else:
            res=[[1/m[0][0]]]
    return res

# промежуточная функция нахождения обратной матрицы(k>2)
def fun1(Sinv,Sk,k):
    X=mul(Sinv,Sk[0:k-1,k-1:k])
    Y=mul(Sk[k-1:k,0:k-1],Sinv)
    O=Sk[k-1][k-1]-mul(Y,Sk[0:k-1,k-1:k])
    if round((Sk[k-1][k-1]-mul(Y,Sk[0:k-1,k-1:k]))[0,0],10)==0:
        res=[[0]]
    else:
        Oinv=invMat(O)
        res1=Sinv+mul(mul(X,Oinv),Y)
        res2=-mul(X,Oinv)
        res3=-mul(Oinv,Y)
        res4=Oinv
        res=np.hstack((np.vstack((res1,res3)),np.vstack((res2,res4))))
    return(res)

def invMain(a):
    if len(a)<2:
        if a[0][0]==0:
            return([[0]])
        else:
            return([[1/a[0][0]]])
    else:
        k=2
        Sk=a[0:k,0:k]
        Sinv=invMat(Sk)
        if np.all(Sinv==[[0]]):
            Sinv=[[0]]
        else:
            while k!=len(a):
                k+=1
                Sk=np.hstack((np.vstack((Sk,a[k-1:k,0:k-1])),a[0:k,k-1:k]))
                Sinv=fun1(Sinv,Sk,k)
    return(Sinv)

def buttonevent():

    p1 = str(coefinput1.get())
    a=mat(p1)

    if np.all((invMain(a))==[[0]]):
        Res1['text']="Обратной матрицы не существует"
        power['text']=''
    else:
        print(len((invMain(a))[0]))
        res=np.zeros((int(len(invMain(a))),int(len((invMain(a))[0]))))
        for i in range(len(invMain(a))):
            for j in range(len((invMain(a))[0])):
                if ((invMain(a)[i][j] * 10) % 10) == 0:
                    res[i][j] = int(invMain(a)[i][j])
                else:
                    res[i][j] = round(invMain(a)[i][j],4)


        Res1['text']=res
        i1=len(invMain(a))
        j1=len((invMain(a))[0])
        power['text']=str(i1)+' x '+str(j1)




def clear():
    power['text']=''
    Res1['text']=''




window = tk.Tk()
window.geometry('+400+200')
window.title('Обратная матрица')

tk.Label(text="Введите матрицу").grid(row=0, column=0, sticky='w', padx=10, pady=5)
coefinput1 = tk.Entry(width=25)
coefinput1.grid(row=0, column=1, sticky='w',columnspan=2, padx=10, pady=5)




tk.Label(text="Размер матрицы A:").grid(row=2, column=0, sticky='e', padx=10, pady=2)
power = tk.Label()
power.grid(row=2, column=1, sticky='w',columnspan=3, padx=10, pady=2)


tk.Label(text="A\U0000207B\U000000B9 = ").grid(row=4, column=0, sticky='e', padx=10, pady=2)
Res1=tk.Label()
Res1.grid(row=4, column=1, sticky='w',columnspan=1, padx=10, pady=2)


tk.Button(text="Вычислить", command=buttonevent,fg='#787878').grid(row=8, column=1, sticky='w', padx=10, pady=2)

tk.Button(text='Очистить', command=clear,fg='#787878').grid(row=8, column=2, sticky='w', padx=10, pady=2)
tk.mainloop()