import numpy as np
# -11 -9 0 0 0 -122; 5 -15 -2 0 0 -48; 0 -8 11 -3 0 14; 0 0 6 -15 4 -50; 0 0 0 3 6 42

# 8 -2 0 0 6; -1 6 -2 0 3; 0 2 10 -4 8; 0 0 -1 6 5
def mat(p):
    mat = []
    for line in p.split(';'):
        mat.append(line.split())
    return np.array(mat).astype(float)



m=str(input())
m=mat(m)
print(m)
a=np.zeros(len(m[0])-1)
b=np.zeros(len(m[0])-1)
c=np.zeros(len(m[0])-1)
d=np.zeros(len(m[0])-1)
a[0]=0
c[len(m[1])-2]=0
for i in range(len(m[0])-1):
    fl=0
    for j in range(len(m[1])):
        if fl==0 and m[i,j]!=0:
            fl=1
            if i==0:
                b[i]=m[i,j]
                c[i]=m[i,j+1]
            elif i==len(m[0])-2:
                a[i]=m[i,len(m[1])-3]
                b[i]=m[i,len(m[1])-2]
            else:
                a[i]=m[i,j]
                b[i]=m[i,j+1]
                c[i]=m[i,j+2]
for i in range(len(m[1])-1):
    d[i]=m[i,len(m[1])-1]
P=np.zeros(len(m[0])-1)
Q=np.zeros(len(m[0])-1)
P[0]=-c[0]/b[0]
Q[0]=d[0]/b[0]
for i in range(1,len(m[0])-1):
    P[i]=-c[i]/(b[i]+a[i]*P[i-1])
    Q[i]=(d[i]-a[i]*Q[i-1])/(b[i]+a[i]*P[i-1])
X=np.zeros(len(m[0])-1)
X[len(m[0])-2]=Q[len(m[0])-2]
for i in range(len(m[0])-3,-1,-1):
    X[i]=round(P[i]*X[i+1]+Q[i],4)
print('Метод прогонки:')
for i in range(len(X)):
    print('x'+str(i)+'='+str(round(X[i],2)))
