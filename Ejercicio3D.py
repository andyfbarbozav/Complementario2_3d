#Barboza Varela Andy Frank
#Complementario de la Unidad 3 de graficacion
import numpy as np
import matplotlib.pyplot as plt
from math import ceil

#   Coordinadas
x=[40,30,80,85]
y=[60,10,60,40]
z=[0,0,0,0]
#   Coordenadas
xg=[]
yg=[]
zg=[]

#   Centro
xc = 80;    yc = 40;    zc = 40

def plotLine(xg,yg,zg):
    plt.axis([80,250,120,20])
    plt.axis()
    plt.grid()
    #Triangulo A
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')
    #Punto 3
    plt.scatter(xg[3],yg[3],s=20,color='r')
    
    plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='r',linestyle=':')
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='r',linestyle=':')
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='r',linestyle=':')

    plt.show()

def hitPoint(x,y,z):
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    Q01=np.sqrt(a*a+b*b+c*c)
    
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    Q12=np.sqrt(a*a+b*b+c*c)
    
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    Q02=np.sqrt(a*a+b*b+c*c)
    
    
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    Q13=np.sqrt(a*a+b*b+c*c)
    
    a=x[2]-x[3]
    b=y[2]-y[3]
    c=z[2]-z[3]
    Q23=np.sqrt(a*a+b*b+c*c)
    
    a=x[0]-x[3]
    b=y[0]-y[3]
    c=z[0]-z[3]
    Q03=np.sqrt(a*a+b*b+c*c)
    #Areas
    s=(Q01+Q12+Q02)/2
    A=np.sqrt(s*(s-Q01)(s-Q12)(s-Q02))

    s1=(Q01+Q03+Q13)/2
    A1=np.sqrt(s1*(s1-Q01)(s1-Q03)(s1-Q13))

    s2=(Q02+Q23+Q03)/2
    A2=np.sqrt(s2*(s2-Q02)(s2-Q23)(s1-Q03))

    return A,A1,A2
    

def plotSquareLine(xc,yc,zc):
    [A,A1,A2]=hitPoint(x,y,z)

    if((A1+A2)>A):
        plt.text(180,80,'OUT')
    elif((A1+A2)<A):
        plt.text(180,80,'IN')

    plotLine(xg,yg,zg)

while True:
    hpx=input('Dame el hitpoint de X? o pulsa w to Exit: ')
    if hpx=='w':
        break
    elif (hpx!=''):
        x[3]=int(hpx)
        hpy=input('Dame el hitpoint de Y?: ')
        y[3]=int(hpy)

        for i in range(len(x)):
            xg.append( x[i]+xc )
            yg.append( y[i]+yc )
            zg.append( z[i]+zc )

        plotSquareLine(xc,yc,zc)
