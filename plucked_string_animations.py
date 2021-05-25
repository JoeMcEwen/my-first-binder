import numpy as np
from numpy import sin, cos, exp, pi
import matplotlib.pyplot as plt

from matplotlib import animation, rc


def animate_plucked_string(d,h,L,T,mass,nx=1000,n=8,dt=.1):
    
    x=np.linspace(0,L,nx)
    
    mu=mass/L
    v=np.sqrt(T/mu)
    
    lam1=2*L
    f1=v/lam1
    T=1/f1
    
    N_frames=int(2*T/dt)
    
    a_n=np.zeros(n) 
    sin_x=np.zeros((n,x.size))
    omega_n=np.zeros(n)

    
    for i in range(n):
        n=i+1
        
        a_n[i]=2*h/n**2/pi**2*L**2/d/(L-d)*sin(d*n*pi/L)
        
        sin_x[i,:]=sin(n*pi*x/L)
        
        omega_n[i]=2*pi*n*f1
        
    fig=plt.figure(figsize=(14,6))
    ax=fig.add_subplot(111)
    ax.set_xlabel("x", size=20)
    ax.set_xlim(0,L)
    ax.set_ylim(-1.5*h,1.5*h)
    ax.grid()
    
    m1,=ax.plot([],[],lw=2, alpha=.5) 
    m2,=ax.plot([],[],lw=2, alpha=.5) 
    m3,=ax.plot([],[],lw=2, alpha=.5) 
    m4,=ax.plot([],[],lw=2, alpha=.5) 
    m5,=ax.plot([],[],lw=2, alpha=.5) 
    m6,=ax.plot([],[],lw=2, alpha=.5) 
    m7,=ax.plot([],[],lw=2, alpha=.5) 
    m8,=ax.plot([],[],lw=2, alpha=.5) 
    m,=ax.plot([],[],lw=4, color="black", alpha=.8) 
    
    plt.close()
    
    
        
    def init():
        m1.set_data([], [])
        m2.set_data([], [])
        m3.set_data([], [])
        m4.set_data([], [])
        m5.set_data([], [])
        m6.set_data([], [])
        m7.set_data([], [])
        m8.set_data([], [])
        m.set_data([], [])
        return m1,m2,m3,m4,m5,m6, m7, m8, m,

    def animate(i):
        
        t=i*dt
        
        y1=a_n[0]*sin_x[0,:]*cos(omega_n[0]*t)
        y2=a_n[1]*sin_x[1,:]*cos(omega_n[1]*t)
        y3=a_n[2]*sin_x[2,:]*cos(omega_n[2]*t)
        y4=a_n[3]*sin_x[3,:]*cos(omega_n[3]*t)
        y5=a_n[4]*sin_x[4,:]*cos(omega_n[4]*t)
        y6=a_n[5]*sin_x[5,:]*cos(omega_n[5]*t)
        y7=a_n[6]*sin_x[6,:]*cos(omega_n[6]*t)
        y8=a_n[7]*sin_x[7,:]*cos(omega_n[7]*t)
        
        m1.set_data(x,y1)
        m2.set_data(x,y2)
        m3.set_data(x,y3)
        m4.set_data(x,y4)
        m5.set_data(x,y5)
        m6.set_data(x,y6)
        m7.set_data(x,y7)
        m8.set_data(x,y8)
        
        y=y1+y2+y3+y4+y5+y6+y7+y8
        
        m.set_data(x,y)
        
        return m1,m2,m3,m4,m5,m6, m7, m8, m,
    
    anim = animation.FuncAnimation(fig, animate, init_func=init,frames=N_frames, interval=40, blit=True)
    return anim 