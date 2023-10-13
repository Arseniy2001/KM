# lambda x:(math.sin(x))**3-(math.cos(x/2))**2 + 2
# -3 3 0.2

# lambda x: -x**4 + 3*x**3 + 4*x-5
# 0 2 0.1

# lambda x:(math.sin(x))**3 - 3*math.sin(x**2) + 4*math.sin(x) + 4*x
# 0 4 0.2

# lambda x: math.log(10 *math.sin((3 * x/5)**2) + 1)
# -3 3 0.005


import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
import tkinter as tk
import math


def sig(Y,k):
    S=0
    for i in range(1,len(Y)+k-3):
        if k==1:
            if i%2==0:
                S=S+Y[i]
        else:
            if i%2!=0:
                S=S+Y[i]
    return S

def buttonevent1():
    start1=float(start.get())
    stop1=float(stop.get())
    step1=float(step.get())

    fx=Yg.get()
    y = lambda x:eval(fx)

    xs= np.arange(start1, stop1+step1, step1)

    Y=np.zeros(len(xs))
    for i in range(len(xs)):
        Y[i]=y(xs[i])
    I=(step1/3)*(Y[0]+Y[len(xs)-1]+4*(sig(Y,2))+2*(sig(Y,1)))

    otv['text']=str(round(I,5))

    ax = plt.gca()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')


    xnew = np.linspace(xs.min(), xs.max(), 300)
    bspline = interpolate.make_interp_spline(xs, Y)
    y_smoothed = bspline(xnew)
    plt.plot(xnew, y_smoothed)

    plt.show()

window = tk.Tk()
window.geometry('+400+200')
window.title('Интегрирование функции по методу Симпсона')

tk.Label(text="Введите функцию").grid(row=0, column=0, sticky='w', padx=10, pady=5)
Yg = tk.Entry(width=30)
Yg.grid(row=0, column=1, sticky='w',columnspan=2, padx=10, pady=5)

tk.Label(text="Введите интервал").grid(row=1, column=0, sticky='w', padx=10, pady=5)
start = tk.Entry(width=10)
start.grid(row=1, column=1, sticky='w', padx=10, pady=5)

stop = tk.Entry(width=10)
stop.grid(row=1, column=2, sticky='w', padx=10, pady=5)

tk.Label(text="Введите шаг").grid(row=2, column=0, sticky='w', padx=10, pady=5)
step = tk.Entry(width=10)
step.grid(row=2, column=1, sticky='w', padx=10, pady=5)

tk.Label(text="Ответ:").grid(row=3, column=0, sticky='w', padx=10, pady=5)
otv = tk.Label()
otv.grid(row=3, column=1, sticky='w', padx=10, pady=5)

tk.Button(text="Построить график", command=lambda :buttonevent1(),fg='#787878').grid(row=8, column=1, sticky='w', padx=10, pady=2)

tk.mainloop()