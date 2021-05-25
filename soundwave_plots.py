import numpy as np
from numpy import sin, cos, exp, pi
import matplotlib.pyplot as plt

from matplotlib import animation, rc


def traveling_soundwave_animation():

    n_p=2000
    n_dots=5
    Lx=8
    Ly=2


    lam=.4*Lx

    k=2*pi/lam
    w=2*pi
    T=2*pi/w
    dt=.01
    n_frames=int(T/dt)
    A=.4
    p_0=-A*w**2/k

    def pressure(x,t):
        return p_0*sin(k*x - w*t)

    def displacement(x,t):
        return A*cos(k*x - w*t)

    x_grid=np.linspace(0,Lx,1000)
    xp=np.random.uniform(0,Lx+1,n_p)
    yp=np.random.uniform(0,Ly,n_p)


    fig=plt.figure(figsize=(14,10))

    ax=fig.add_subplot(311)
    ax.set_xlim(-A,Lx)
    ax.set_ylim(0,Ly)

    pts,=ax.plot([],[],"o",color="black")
    dots,=ax.plot([],[],"o",color="red")
    wall,=ax.plot([], [],lw=6,color="black",alpha=.5)

    ax=fig.add_subplot(312)
    ax.set_xlim(-A,Lx)
    ax.set_ylim(-1.5*A,1.5*A)
    ax.axes.get_yaxis().set_visible(False)
    ax.axvline(0,lw=4,color="black",alpha=.5)
    ax.grid()

    ln,=ax.plot([],[],lw=4,color="blue",label="displacement")
    sdt, =ax.plot([],[],"o",markersize=10,color="blue",alpha=.8)
    ax.legend(fontsize="xx-large",loc=3)

    ax=fig.add_subplot(313)
    ax.set_xlim(-A,Lx)
    ax.set_ylim(-1.5*p_0,1.5*p_0)
    ax.axvline(0,lw=4,color="black",alpha=.5)
    ax.grid()
    ax.axes.get_yaxis().set_visible(False)

    pres,=ax.plot([],[],lw=4,color="red",alpha=.8,label="pressure")
    p1dt,=ax.plot([],[],"o",markersize=10,color="red")
    p2dt,=ax.plot([],[],"o",markersize=10,color="red")

    ax.legend(fontsize="xx-large",loc=3)
    plt.close()

    def init():
        ln.set_data([],[])
        pts.set_data([],[])
        dots.set_data([],[])
        wall.set_data([],[])
        pres.set_data([],[])
        sdt.set_data([],[])
        p1dt.set_data([],[])
        p2dt.set_data([],[])

        return ln,pts,dots, wall,pres, sdt, p1dt, p2dt,
    
    def animate(i):
        #global x, y

        t=i*dt

        sm= displacement(x_grid,t)
        ln.set_data(x_grid,sm)

        sm=xp+displacement(xp,t)
        pts.set_data(sm[n_dots:],yp[n_dots:])
        dots.set_data(sm[:n_dots],yp[:n_dots])

        sm=displacement(0,t)
        wall.set_data([sm,sm],[0,Ly])

        p=pressure(x_grid,t)
        pres.set_data(x_grid,p)
    
        sm=displacement(4,t)
        sdt.set_data([4],[sm])

        p=pressure(3.8,t)
        p1dt.set_data([3.8],[p])

        p=pressure(4.2,t)
        p2dt.set_data([4.2],[p])

        return ln, pts, dots, wall, pres,sdt, p1dt, p2dt,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=n_frames, interval=150, blit=True)
    
    return anim

def sound_reflection_animation():
    
    n_p=2000
    Lx=8
    Ly=2

    v=15
    n_frames=100
    
    T=Lx/v
    dt=.01
    A=.5
    n_frames=int(2*T/dt)
    
    #print("frames",n_frames)
    
    def gauss_pulse(x,t):
        # This is a hack, need a better way
        # currently adds to waves moving left and right, with the right ward
        # moving wave started at the right at 2L
        yl=A*exp(-(x-v*t)**2/.5)
        yr=-A*exp(-(x -2*Lx +v*t)**2/.5)
        
        return yl+yr

    x_grid=np.linspace(0,Lx,1000)
    xp=np.random.uniform(0,Lx,n_p)
    yp=np.random.uniform(0,Ly,n_p)
    
    fig=plt.figure(figsize=(14,10))

    ax=fig.add_subplot(211)
    ax.set_xlim(0,Lx)
    ax.set_ylim(0,Ly)

    pts,=ax.plot([],[],"o",color="black")
    wall,=ax.plot([],[],lw=6,color="black",alpha=.6)
    ax.axvline(Lx,lw=6,color="black", alpha=.6)
    

    ax=fig.add_subplot(212)
    ax.set_xlim(0,Lx)
    ax.set_ylim(-1.5*2*A,1.5*2*A)
    ax.axes.get_yaxis().set_visible(False)
    ax.axvline(0,lw=4,color="black",alpha=.5)
    ax.grid()

    pulse,=ax.plot([],[],lw=4,color="blue",label="displacement")
    ax.legend(fontsize="xx-large",loc=3)
    

    plt.close()

    def init():
        pulse.set_data([],[])
        pts.set_data([],[])
        wall.set_data([],[])
        

        return pulse,pts,wall, 
 
    def animate(i):
        #global x, y

        t=i*dt
        
        y= gauss_pulse(x_grid,t)
        pulse.set_data(x_grid,y)
    
        sm=xp+gauss_pulse(xp,t)
        pts.set_data(sm,yp)
        
        sm=gauss_pulse(0,t)
        wall.set_data([sm,sm],[0,Ly])
        
        return pulse, pts,wall, 

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=n_frames, interval=175, blit=True)
    return anim

def sound_standingwave_animation(n,wtype="CO"):
    
    if wtype not in ["OO", "OC", "CC"]:
        raise ValueError("Must select wtype from OO, OC, CC.")
    
    if n <=0:
        raise ValueError("n must be greater than 0.")
        
    if n>=8:
        raise ValueError("Whoa there cowboy! Let's not get too crazzy with n and break our animaiton. n >= 8 please.")
        

    n_p=1500
    Lx=8
    Ly=2

    v=10
    
    if wtype=="OC":
        if n%2 ==0: 
            raise ValueError("For a closed-open tube, n must be odd.")
        lam=4*Lx/n
        f=n*v/4/Lx
        
    elif wtype=="OO" or wtype=="CC":
        lam=2*Lx/n
        f=n*v/2/Lx
    if wtype=="CC":
        phi=pi/2
    else:
        phi=0
        

    k=2*pi/lam
    w=2*pi*f
    T=2*pi/w
    dt=.01
    n_frames=int(T/dt)
    
    
    #print("number of frames", n_frames)

    A=.2
    p_0=-A*w**2/k


    def standing_pressure(x,t):
        return 2*p_0*sin(k*x - phi)*cos(w*t)

    def standing_displacement(x,t):
    
        return 2*A*cos(k*x - phi)*cos(w*t)

    x_grid=np.linspace(0,Lx,1000)
    xp=np.random.uniform(-1,Lx+1,n_p)
    yp=np.random.uniform(0,Ly,n_p)
    
#     # calculate nodes
#     # kx - phi = n pi/2
#     # x= (n pi/2 + phi)/k
#     nodes=(np.arange(1,n+1)*pi/2 + phi)/k 
   
#     # calculate anti-nodes
#     # kx - phi = n 2*pi
#     # x= (n pi/2 + phi)/k
#     #anti_notes=

    fig=plt.figure(figsize=(14,7))

    ax=fig.add_subplot(311)
    ax.set_xlim(0,Lx)
    ax.set_ylim(0,Ly)

    pts,=ax.plot([],[],"o",color="black")
    dots,=ax.plot([],[],"o",color="red")
    ax.axhline(0,lw=10,color="blue")
    ax.axhline(Ly,lw=10,color="blue")
    
    if wtype=="CC":
        ax.axvline(0,lw=10,color="blue")
        ax.axvline(Lx,lw=10,color="blue")
    
    if wtype=="OC":
        ax.axvline(Lx,lw=10,color="blue")
       
    
    #wall,=ax.plot([], [],lw=6,color="black",alpha=.5)

    ax=fig.add_subplot(312)
    ax.set_xlim(0,Lx)
    ax.set_ylim(-1.5*2*A,1.5*2*A)
    ax.axes.get_yaxis().set_visible(False)
    ax.grid()

    ln,=ax.plot([],[],lw=4,color="blue",label="displacement")
    l0= standing_displacement(x_grid,0)
    ax.plot(x_grid,l0,lw=2,color="blue",alpha=.5)
    ax.legend(fontsize="xx-large",loc=3)

    ax=fig.add_subplot(313)
    ax.set_xlim(0,Lx)
    ax.set_ylim(-1.5*2*p_0,1.5*2*p_0)
    ax.grid()
    ax.axes.get_yaxis().set_visible(False)

    pres,=ax.plot([],[],lw=4,color="red",alpha=.8,label="pressure")
    p0=standing_pressure(x_grid,0)
    ax.plot(x_grid,p0,lw=2,color="red",alpha=.3)

    ax.legend(fontsize="xx-large",loc=3)
    plt.close()

    def init():
        ln.set_data([],[])
        pts.set_data([],[])
        pres.set_data([],[])

        return ln, pts,pres,
 
    def animate(i):
        #global x, y

        t=i*dt
        
        sm= standing_displacement(x_grid,t)
        ln.set_data(x_grid,sm)
    
        sm=xp+standing_displacement(xp,t)
        pts.set_data(sm,yp)
        
        p=standing_pressure(x_grid,t)
        pres.set_data(x_grid,p)

    
        return ln, pts,pres,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=n_frames, interval=175, blit=True)
    return anim


