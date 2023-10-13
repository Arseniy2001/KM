import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
import tkinter as tk
from scipy.interpolate import interp1d
# -0.008, -0.066, -0.209, -0.439, -0.734, -1.044, -1.31, -1.484, -1.542, -1.491, -1.366, -1.218, -1.093, -1.02, -0.998, -1, -0.982, -0.901, -0.733, -0.479, -0.174, 0.128, 0.372, 0.513, 0.537, 0.46, 0.323, 0.177, 0.065, 0.009, -0.002
# -3 3 0.2

# -5, -4.597, -4.178, -3.727, -3.234, -2.688, -2.082, -1.411, -0.674, 0.131, 1, 1.929, 2.91, 3.935, 4.99, 6.063, 7.134, 8.187, 9.198, 10.145, 11
# 0 2 0.1

# 0, 1.483, 2.739, 3.782, 4.647, 5.437, 6.363, 7.723, 9.749, 12.314, 14.659, 15.538, 14.109, 11.222, 9.578, 11.331, 14.75, 15.096, 11.393, 9.66, 13.403
# 0 4 0.2

# -4.045, 1.782, 2.279, 2.398, 2.322, 2.109, 1.784, 1.355, 0.83, 0.281, 0, 0.281, 0.83, 1.355, 1.784, 2.109, 2.322, 2.398, 2.279, 1.782, -4.045
# -3 3 0.3

def Diff(Y,h):
    m=np.zeros((len(Y),len(Y)))
    for i in range(len(m)):
        m[i,0]=Y[i]
    for j in range(1,len(m)):
        for i in range(len(m)-j):
            m[i,j]=m[i+1,j-1]-m[i,j-1]
    Y2=np.zeros(len(m))
    for i in range(len(m)):
        for j in range (1,5):
            Y2[i]+=(m[i,j]/j)*pow(-1,j+1)
        Y2[i]=Y2[i]/h
    return (Y2)


def fun(X1,Y1,Y2):

    xnew = np.linspace(X1.min(), X1.max(), 300)
    bspline = interpolate.make_interp_spline(X1, Y2)
    y_smoothed = bspline(xnew)


    bspline2 = interpolate.make_interp_spline(X1, Y1)
    y_smoothed2 = bspline2(xnew)
    plt.plot(xnew, y_smoothed2)
    plt.plot(xnew, y_smoothed)
    plt.legend(['F(x)', 'F′(x)'], loc='best')

    ax = plt.gca()

    # plot X - axis
    ax.axhline(y=0, color='k')

    # plot Y - axis
    ax.axvline(x=0, color='k')
    plt.show()


def buttonevent1():
    start1=float(start.get())
    stop1=float(stop.get())
    step1=float(step.get())
    X1 = np.arange(start1, stop1+step1, step1)
    Y1= [float(a) for a in Yg.get().split(", ")]
    Y2=Diff(Y1,step1)
    fun(X1,Y1,Y2)


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

tk.Button(text="Построить график", command=lambda :buttonevent1(),fg='#787878').grid(row=8, column=1, sticky='w', padx=10, pady=2)

tk.mainloop()