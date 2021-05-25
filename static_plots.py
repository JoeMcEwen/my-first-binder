import numpy as np
import matplotlib.pyplot as plt

from numpy import sin, cos, exp, pi

def mystery_harmonics():
    '''
    problem for students
    '''
    
    nx=1000
    L=1
    
    x=np.linspace(0,L,nx)
    
    k=2*pi/L
    
    n=[2,5,7]
    labels=["A", "B", "C"]
    
    fig=plt.figure(figsize=(14,6))
    ax=fig.add_subplot(111)
    ax.set_xlim(0,L)
    for i in range(3):
        
        label=labels[i]
    
        
        ax.plot(x,sin(k*n[i]*x),lw=4, alpha=.5, label=label)
    ax.legend(fontsize="xx-large",loc=3)
    ax.grid()
    plt.close()
    
    return fig 

def periodic_sawtooth():
    '''
    plot sawtooth function
    '''
    
    nx=100
    L=1
    A=1
    
    x=np.linspace(0,L,nx)
    y=A*x
    
    fig=plt.figure(figsize=(14,6))
    ax=fig.add_subplot(111)
    ax.set_xlim(-3*L/2,3*L/2)
    ax.set_title("periodic sawtooth function",size=20)
    ax.set_xlabel("x", size=20)
    
    ax.plot(x-L,y,lw=4, color="blue")
    ax.plot(x,y,lw=4, color="blue")
    ax.plot([0,0],[A,0], lw=4, color="black",alpha=.5)
    ax.plot(x+L,y,lw=4, color="blue")
    ax.plot([L,L],[A,0], lw=4, color="black",alpha=.5)
    ax.plot([-L,-L],[A,0], lw=4, color="black",alpha=.5)
    ax.plot([2*L,2*L],[A,0], lw=4, color="black",alpha=.5)
    ax.plot(x[int(nx/2):]-2*L,y[int(nx/2):],lw=4, color="blue")
    ax.plot(x[:int(nx/2)] +2*L,y[:int(nx/2)],lw=4, color="blue")
    
    
    
    ax.grid()
    plt.close()
    
    return fig 
    
def sawtooth_static_plot():
    '''
    plot sawtooth function
    '''
    
    nx=1000
    L=1
    A=1
    x=np.linspace(-L/2,L/2,nx)
    y=A*x
    
    n_h=50
    harmonics=np.zeros((n_h,x.size))
    
    for i in range(n_h):
        
        n=i + 1
        
        bn=(-1)**(n+1)*A/pi/n
        kn=2*n*pi/L
        
        harmonics[i,:]=bn*sin(kn*x)
    
    
    
    fig=plt.figure(figsize=(14,6))
    
    ax=fig.add_subplot(221)
    ax.set_xlim(-3*L/2,3*L/2)
    ax.set_title(r"$n=1$",size=20)
    
    h=harmonics[0,:]
    
    ax.plot(x,y,color="blue")
    ax.plot(x-L,y,color="blue")
    ax.plot(x+L,y,color="blue")
    ax.axvline(-L/2,color="black",alpha=.5)
    ax.axvline(L/2,color="black",alpha=.5)
    ax.plot(x,h,color="orange")
    ax.plot(x-L,h,color="orange")
    ax.plot(x+L,h,color="orange")
    ax.grid()

    
    ax=fig.add_subplot(222)
    ax.set_xlim(-3*L/2,3*L/2)
    ax.set_title(r"$n=5$",size=20)
    
    
    h=np.sum(harmonics[:5,:],axis=0)
    
    ax.plot(x,y,color="blue")
    ax.plot(x-L,y,color="blue")
    ax.plot(x+L,y,color="blue")
    ax.axvline(-L/2,color="black",alpha=.5)
    ax.axvline(L/2,color="black",alpha=.5)
    ax.plot(x,h,color="orange")
    ax.plot(x-L,h,color="orange")
    ax.plot(x+L,h,color="orange")
    ax.grid()
    
    ax=fig.add_subplot(223)
    ax.set_xlim(-3*L/2,3*L/2)
    ax.set_title(r"$n=20$",size=20)
    ax.set_xlabel("x", size=20)
    
    h=np.sum(harmonics[:20,:],axis=0)
    
    ax.plot(x,y,color="blue")
    ax.plot(x-L,y,color="blue")
    ax.plot(x+L,y,color="blue")
    ax.axvline(-L/2,color="black",alpha=.5)
    ax.axvline(L/2,color="black",alpha=.5)
    ax.plot(x,h,color="orange")
    ax.plot(x-L,h,color="orange")
    ax.plot(x+L,h,color="orange")
    ax.grid()
    
    
    ax=fig.add_subplot(224)
    ax.set_xlim(-3*L/2,3*L/2)
    ax.set_title(r"$n=50$",size=20)
    ax.set_xlabel("x", size=20)
    
    h=np.sum(harmonics,axis=0)
    
    ax.plot(x,y,color="blue")
    ax.plot(x-L,y,color="blue")
    ax.plot(x+L,y,color="blue")
    ax.axvline(-L/2,color="black",alpha=.5)
    ax.axvline(L/2,color="black",alpha=.5)
    ax.plot(x,h,color="orange")
    ax.plot(x-L,h,color="orange")
    ax.plot(x+L,h,color="orange")
    ax.grid()
    plt.tight_layout()
    plt.close()
    return fig
    
