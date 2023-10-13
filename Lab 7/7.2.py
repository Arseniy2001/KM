import numpy as np
import math
import matplotlib.pyplot as plt
import pylab

# Метод Эйлера
def el(x,y0,yt0,h,ytt):
    Y=np.zeros(len(x))
    Y[0]=y0
    Yt=np.zeros(len(x))
    Yt[0]=yt0
    for i in range(1,len(Y)):
        Y[i]=Y[i-1]+h*Yt[i-1]
        Yt[i]=Yt[i-1]+h*ytt(x[i-1],Y[i-1])
    return(Y)

# Метод Эйлера с пересчетом
def elper(x,y0,yt0,h,ytt):
    Y=np.zeros(len(x))
    Y[0]=y0
    Yt=np.zeros(len(x))
    Yt[0]=yt0
    for i in range(1,len(Y)):
        Y[i]=Y[i-1]+h/2*(2*Yt[i-1]+h*ytt(x[i-1],Y[i - 1]))
        Yt[i]=Yt[i-1]+h/2*(ytt(x[i-1],Y[i-1])+ytt(x[i-1]+h,Y[i-1]+h*ytt(x[i-1],Y[i-1])))
    return(Y)

# Метод Рунге — Кутты
def ruku(x,y0,yt0,h,ytt):
    Y=np.zeros(len(x))
    Y[0]=y0
    Yt=np.zeros(len(x))
    Yt[0]=yt0
    for i in range(1,len(Y)):
        Y[i]=Y[i-1]+h*Yt[i-1]
        k1=ytt(x[i-1],Y[i-1])
        g1=Yt[i-1]
        k2=ytt(x[i-1]+h/2,Y[i-1]+h/2*k1)
        g2=Yt[i-1]+h*k1/2
        k3=ytt(x[i-1]+h/2,Y[i-1]+h/2*k2)
        g3=Yt[i-1]+h*k2/2
        k4=ytt(x[i-1]+h,Y[i-1]+h*k3)
        g4=Yt[i-1]+h*k3
        Y[i]=Y[i-1]+h/6*(g1+2*g2+2*g3+g4)
        Yt[i]=Yt[i-1]+h/6*(k1+2*k2+2*k3+k4)
    return(Y,Yt)

# Метод Адамса
def adams(x,y0,yt0,h,ytt):

    ruku4 = ruku(x,y0,yt0,h,ytt)[0]
    ruku4t =ruku(x,y0,yt0,h,ytt)[1]
    Y=np.zeros(len(x))
    Y[0]=y0
    Yt=np.zeros(len(x))
    Yt[0]=yt0
    for i in range(1,4):
        Y[i]=ruku4[i]
        Yt[i]=ruku4t[i]
    for i in range(4, len(Y)):
        Y[i]=Y[i-1]+h/24*(55*Yt[i-1]-59*Yt[i-1]+37*Yt[i-1]-9*Yt[i-1])
        Yt[i]=Yt[i-1]+h/24*(55*ytt(x[i-1]-h,Y[i - 1])-59*ytt(x[i-1]-2*h, Y[i - 2])+37*ytt(x[i-1]-3*h,Y[i - 3])-9*ytt(x[i-1]-4*h,Y[i - 4]))

    return(Y)

y=lambda x: math.cos(x)+11/8*math.sin(x)-math.sin(3*x)/8
ytt=lambda x,y: -y+math.sin(3*x)
y0=1
yt0=1
h=0.1
xmin=0
xmax=50
# y=lambda x: (1 + x) * (math.e ** (-x**2))
# yt=lambda x: math.e ** (-x ** 2) - 2 * x * (1 + x) * (math.e ** (-x ** 2))
# ytt=lambda x,y: -4 * x * yt(x) - (4 * (x ** 2) + 2) * y
# y0=1
# yt0=1
# h=0.1
# xmin=0
# xmax=3.5

x = np.arange(xmin, xmax+h, h)
pylab.plot(x, [y(t) for t in x], 'blue', label="Точное решение")
pylab.plot(x,el(x,y0,yt0,h,ytt),'red',label="Метод Эйлера")
pylab.plot(x,elper(x,y0,yt0,h,ytt),'purple',label="Метод Эйлера c пересчетом")
pylab.plot(x,ruku(x,y0,yt0,h,ytt)[0],'green',label="Метод Рунге — Кутты")
pylab.plot(x,adams(x,y0,yt0,h,ytt),'yellow',label="Метод Адамса")
plt.legend(loc=2, prop={'size': 8})


plt.show()