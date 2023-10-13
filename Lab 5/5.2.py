# coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 2 1 -4 ; -3 4 0 ; -3 -1 8
# 1 -3 -2 ; -1 4 4 ; -2 3 6
# -1 7 2 ; 9 8 1 ; 5 2 7
# -10 1 -1 ; -4 -8 -1 ; -2 -5 -9
#  4 1 0 ; 1 2 1 ; 0 1 1
import math
import numpy as np

def mat(p):
    mat = []
    for line in p.split(';'):
        mat.append(line.split())
    return np.array(mat).astype(float)
# нахождение следа матрицы
def getS(m1,n):
    k=1
    m2=m1.copy()
    while k!=n:
        k+=1
        m2=m2@m1
    s=0
    for i in range(len(m2)):
        s+=m2[i,i]
    return(s)

def Fun(m):
    y=[[3],[4],[1]]
    n=1
    y1=getS(m,n)
    y2=getS(m,n+1)
    y3=getS(m,n+2)
    print(y2/y1)
    # print(y3/y2)
    eps=0.0001
    while abs((y2/y1-y3/y2)/2)>eps:
        n+=1
        print(y2/y1)
        y1=getS(m,n)
        y2=getS(m,n+1)
        y3=getS(m,n+2)
    # print(y3/y2)



print("Введите матрицу 1")
p1=input()
a=mat(p1)
Fun(a)





# n=1
# a1=np.linalg.matrix_power(a, n)
# a2=np.linalg.matrix_power(a, n+1)
# a3=np.linalg.matrix_power(a, n+2)
# y1=a1@y
# y2=a2@y
# y3=a3@y
# eps=0.001
# while abs(((y2[0,0]/y1[0,0]+y2[1,0]/y1[1,0]+y2[2,0]/y1[2,0])/3)-(y3[0,0]/y2[0,0]+y3[1,0]/y2[1,0]+y3[2,0]/y2[2,0])/3)>eps:
#     n+=1
#     a1=np.linalg.matrix_power(a, n)
#     a2=np.linalg.matrix_power(a, n+1)
#     a3=np.linalg.matrix_power(a, n+2)
#     y1=a1@y
#     y2=a2@y
#     y3=a3@y
# print((y3[0,0]/y2[0,0]+y3[1,0]/y2[1,0]+y3[2,0]/y2[2,0])/3)