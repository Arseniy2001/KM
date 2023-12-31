import numpy as np
# 19 -4 -9 -1 100; -2 20 -2 -7 -5; 6 -5 -25 9 34; 0 -3 -9 12 69
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

def compare(xn,xol,eps):
    c=0
    for i in range(len(xn)):
        if abs(xn[i,0]-xol[i,0])>eps[i,0]:
            c=1
    return(c)

def iter(a,b,eps,xol,xn):
    v=0
    while compare(xn,xol,eps)!=0:
        v+=1
        xn,xol=a@xol+b,xn

    for i in range(len(xn)):
        xn[i,0]=round(xn[i,0],1)
    for i in range(len(xn)):
        print('x'+str(i)+'='+str(round(xn[i,0],2)))
    print('Количество итераций: '+str(v))
def zed(a,b,eps,xol,xn):

    sr=np.copy(xol)
    v=0
    while compare(xn,sr,eps)!=0:
        v+=1
        sr=np.copy(xn)
        xn=np.zeros((len(m),1))
        for i in range(len(xn)):
            if i!=0:
                xol[i-1,0]=xn[i-1,0]
            for j in range(len(xn)):
                xn[i,0]+=a[i,j]*xol[j,0]
            xn[i,0]+=b[i,0]
        xol[i,0]=xn[i,0]
    for i in range(len(xn)):
        xn[i,0]=round(xn[i,0],1)
    for i in range(len(xn)):
        print('x'+str(i)+'='+str(round(xn[i,0],2)))
    print('Количество итераций: '+str(v))

m=str(input())
m=mat(m)
print(m)

a=np.zeros((len(m),len(m)))
b=np.zeros((len(m),1))
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            a[i,j]=-m[i,j]/m[i,i]
        else:
            a[i,j]=0
    b[i]=m[i,len(m)]/m[i,i]
eps=np.full((len(m),1),0.01)
xol=np.copy(b)
xn=np.zeros((len(m),1))

print('Метод простых итераций:')
iter(a,b,eps,xol,xn)
print('Метод Зейделя:')
zed(a,b,eps,xol,xn)
