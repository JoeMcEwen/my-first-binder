import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, exp, pi
import ipywidgets as widgets
from ipywidgets import interact, IntSlider, FloatSlider


n=100
T=1/262
n_t=1000
t=np.linspace(0,T,n_t)
bn=np.zeros(n)
wn=np.zeros(n)
hn=np.zeros((n,t.size))

for i in range(n):
    j=i+ 1
    
    wn[i]=2*j*pi/T
    
    bn[i]=2/j/pi*(-15/8*cos(j*pi/2) + 1 +7/8*(cos(j*pi)))
    
    hn[i]=bn[i]*sin(wn[i]*t)
    
    
def soundwave_Fourier_plot(n):
    
    fig=plt.figure(figsize=(10,6))
    ax=fig.add_subplot()
    ax.set_xlabel("time", size=20)
    ax.set_ylabel(r"$P(t)$",size=20)

    p=np.ones(int(n_t/4))
    p=np.r_[p, -7/8*p, 7/8*p, -p]
    ax.set_xlim(t[0],t[-1])

    f=np.sum(hn[:n,:],axis=0)

    ax.axhline(0,color="black",alpha=.5)
    ax.plot(t,p,lw=4,color="black")
    ax.plot(t,f)
    ax.grid()
    plt.close()
    
    return fig

def soundwave_interactive():
    
    n_widget=IntSlider(value=1,min=1,max=100, description="n terms")
    return interact(soundwave_Fourier_plot,n=n_widget)
    
    
def pressure_plot():
    fig=plt.figure(figsize=(10,6))
    ax=fig.add_subplot()
    ax.set_xlabel("time", size=20)
    ax.set_ylabel(r"$P(t)$",size=20)

    T=1/262
    n=1000
    t=np.linspace(-2*T,2*T,4*n)
    p=np.ones(int(n/4))
    p=np.r_[p, -7/8*p, 7/8*p, -p]

    p=np.r_[p,p,p,p]

    ax.set_xlim(t[0],t[-1])

    ax.axhline(0,color="black",alpha=.5)
    ax.axvline(0,color="black", alpha=.5)
    ax.plot(t,p,lw=4,color="blue", alpha=.8)
    ax.grid()
    plt.close()
    
    return fig