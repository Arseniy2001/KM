import numpy as np
import math
import matplotlib.pyplot as plt
import pylab



# Метод Эйлера
def el(x,y0,h,yt):
    Y=np.zeros(len(x))
    Y[0]=y0
    for i in range(1,len(Y)):
        Y[i]=Y[i-1]+h*yt(x[i-1],Y[i-1])
    return(Y)


# Метод Эйлера с пересчетом
def elper(x,y0,h,yt):
    Y=np.zeros(len(x))
    Y[0]=y0
    for i in range(1,len(Y)):
        Y[i]=Y[i-1]+h/2*(yt(x[i-1],Y[i-1])+yt(x[i-1]+h,Y[i-1]+h*yt(x[i-1],Y[i-1])))
    return(Y)


# Метод Рунге — Кутты
def ruku(x,y0,h,yt):
    Y=np.zeros(len(x))
    Y[0]=y0
    for i in range(1,len(Y)):
        k1=yt(x[i-1],Y[i-1])
        k2=yt(x[i-1]+h/2,Y[i-1]+h/2*k1)
        k3=yt(x[i-1]+h/2,Y[i-1]+h/2*k2)
        k4=yt(x[i-1]+h,Y[i-1]+h*k3)
        Y[i]=Y[i-1]+h/6*(k1+2*k2+2*k3+k4)
    return(Y)


# Метод Адамса
def adams(x,y0,h,yt):

    ruku4 = ruku(x,y0,h,yt)
    Y=np.zeros(len(x))
    Y[0]=y0
    for i in range(1,4):
        Y[i]=ruku4[i]
    for i in range(4, len(Y)):
        Y[i]=Y[i-1]+h/24*(55*yt(x[i-1]-h,Y[i - 1])-59*yt(x[i-1]-2*h, Y[i - 2])+37*yt(x[i-1]-3*h,Y[i - 3])-9*yt(x[i-1]-4*h,Y[i - 4]))
    return(Y)

y=lambda x: (math.e**x)/2+math.e**-x
yt=lambda x,y: -y+(math.e)**x
y0=1.5
h=0.1
xmin=0
xmax=1

x = np.arange(xmin, xmax+h, h)
pylab.plot(x, [y(t) for t in x], 'blue', label="Точное решение")
pylab.plot(x,el(x,y0,h,yt),'red',label="Метод Эйлера")
pylab.plot(x,elper(x,y0,h,yt),'purple',label="Метод Эйлера c пересчетом")
pylab.plot(x,ruku(x,y0,h,yt),'green',label="Метод Рунге — Кутты")
pylab.plot(x,adams(x,y0,h,yt),'yellow',label="Метод Адамса")
plt.legend(loc=2, prop={'size': 8})


plt.show()