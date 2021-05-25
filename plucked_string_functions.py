import numpy as np
from numpy import sin, cos, exp, pi

import matplotlib.pyplot as plt
from matplotlib import animation, rc

def make_static_mode_plot():
    
    nx=1000
    
    n=[1,3,6]
    L=4
    
    x=np.linspace(0,L,nx)
    
    fig=plt.figure(figsize=(14,6))
    ax=fig.add_subplot(111)
    ax.set_xlim(0,L)
    
    for i in range(len(n)):
        
        k=n[i]*pi/L
        
        y=sin(k*x)
        
        ax.plot(x,y,lw=4,alpha=.8)
        
    ax.grid()
    ax.set_xlabel("centimeters", size=20)
    ax.set_ylabel("nano meters",size=20)
    
def ic_plot():
    
    L=4
    h=.6
    d=.75
    m1=h/d
    m2=-h/(L-d)
    x1=np.linspace(0,d,100)
    x2=np.linspace(d,L,100)
    
    y1=m1*x1
    y2=m2*(x2-d) + h
    
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlabel("x", size=20)
    
    ax.plot(x1,y1,lw=4,color="black",alpha=.8)
    ax.plot(x2,y2,lw=4,color="black",alpha=.8)
    ax.grid()
    plt.close()
    
    return fig

def animate_mode(n):
    
    omega=1
    L=4
    dt=.1
    
    N_frames=int(2*(2*pi/omega/dt))
    
    k=n*pi/L
    x=np.linspace(0,L,400)
    
    sine_part=sin(k*x)
    
    fig=plt.figure(figsize=(14,6))
    ax=fig.add_subplot(111)
    ax.set_xlim(0,L)
    ax.set_ylim(-1.5,1.5)
    ax.set_xlabel("x", size=20)
    ax.set_ylabel(r"$y(x,t)$", size=20)
    
    line,=ax.plot([],[],lw=4,color="blue",alpha=.8)
    
    ax.grid()
    plt.close()
    

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        
        t=i*dt
        y = cos(omega*t)*sine_part
        
        line.set_data(x, y)
        return line,
    
    anim = animation.FuncAnimation(fig, animate, init_func=init,frames=N_frames, interval=40, blit=True)
    
    return anim