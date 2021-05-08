import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, exp, pi
import ipywidgets as widgets
from ipywidgets import interact, IntSlider, FloatSlider

def plot_sin_harmonic(n,nx=1000,L=1):
    '''
    plots sin harmonic \n
    always plots fundamental 
    '''
    
    x=np.linspace(0,L,nx)
    
    k=2*pi/L
    
    fig=plt.figure(figsize=(14,6))
    
    ax=fig.add_subplot(111)
    ax.set_xlim(0,L)
    
    if n==1:
        
        label=str(n) + "st harmonic"
    elif n==2:
        label=str(n) + "nd harmonic"
    
    elif n==3:
        label=str(n) + "rd harmonic"
        
    else:
        label=str(n) + "th harmonic"
    
    ax.plot(x,sin(k*x),lw=4,alpha=.5,label="fundamental")
    ax.plot(x,sin(k*n*x),lw=4, label=label)
    ax.legend(fontsize="xx-large",loc=3)
    ax.grid()
    plt.close()
    
    return fig 

def sin_harmonic_interactive():
    
    n_widget=IntSlider(value=3,min=0,max=20, description="harmonic:")
    nx_widget=IntSlider(value=500,min=0,max=1000, description="grid points:")
    L_widget=FloatSlider(value=1,min=1,max=5,description="length L")

    return interact(plot_sin_harmonic,n=n_widget,nx=nx_widget,L=L_widget)


def sawtooth(n,A,L,x):
    
    bn=np.zeros(n)
    fourier_terms=np.zeros((n,x.size))
    k=pi/L
    
    for i in range(n):
        j=i+1
        
        bn[i]=(-1)**(j+1)*2*A*L/pi/j
        fourier_terms[i,:]=bn[i]*sin(k*j*x)
        
    return bn, fourier_terms


def plot_sawtooth_interactive(n,A):
    
    nx=1000
    L=1
    
    x=np.linspace(0,L,nx)
    
    bn,fourier_terms=sawtooth(n,A,L,x)
    
    f=np.sum(fourier_terms,axis=0)
    f_true=A*x
    fig=plt.figure(figsize=(14,6))
    ax=fig.add_subplot(111)
    ax.set_xlim(0,L)
    
    label="Fourier approx., n=" + str(n)
    
    ax.plot(x,f_true,lw=4, alpha=.5, label="true")
    ax.plot(x,f,lw=4,label=label)
    ax.legend(fontsize="xx-large",loc=2)
    ax.grid()
    plt.close()
    
    return fig 
    
def sawtooth_interactive():
    
    n_widget=IntSlider(value=10,min=1,max=100, description="n terms")
    
    A_widget=FloatSlider(value=1,min=-3,max=3,description="slope")
    
    return interact(plot_sawtooth_interactive,n=n_widget,A=A_widget)
    
    
    