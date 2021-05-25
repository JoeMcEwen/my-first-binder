import numpy as np
from numpy import sin, cos, exp, pi

mu=1e-6
C=200*mu
V=90
R=10000
tau=R*C
V_b=80
V_e=40
t_e=-tau*np.log((V-V_e)/V)
T=R*C*np.log((V-V_e)/(V-V_b))
nt=1000

data_dict={}
data_dict["capacitor"]=C
data_dict["batter voltage"]=V
data_dict["resistor"]=R
data_dict["time constant"]=tau
data_dict["breakdown voltage"]=V_b
data_dict["extinction voltage"]=V_e
data_dict["period"]=T
data_dict["extinction time"]=t_e

nt=1000
t=np.linspace(0,5*T,nt)
dt=t[1]-t[0]
Vn=np.zeros(t.size)

def voltage(t):
    return V*(1-exp(-t/tau))

t_eval=0
for i in range(nt):
    
    v=voltage(t_eval)
    
    if v >=V_b:
        #print(t_eval,t[i])
        t_eval=t_e
        v=voltage(t_eval)
    Vn[i]=v
    
    t_eval+=dt
    
data_dict={}
data_dict["capacitor"]=C
data_dict["batter voltage"]=V
data_dict["resistor"]=R
data_dict["time constant"]=tau
data_dict["breakdown voltage"]=V_b
data_dict["extinction voltage"]=V_e
data_dict["period"]=T
data_dict["extinction time"]=t_e
data_dict["voltage data"]={"voltage":Vn, "time":t}


t=np.linspace(0,T,1000)
# make periodic data 
v=V*(1-exp(-(t+t_e)/tau))
t=np.r_[t, t+T, t+2*T, t + 3*T]
v=np.r_[v,v,v,v]
data_dict["periodic voltage data"]={"voltage":v, "time":t}


# make Fourier data 
nmax=500

n=np.arange(1,nmax+1)
an=np.zeros(nmax)
bn=np.zeros(nmax)
wn=np.zeros(nmax)
hn=np.zeros((nmax,t.size))

pf=-2*V/T*exp(-t_e/tau)

for i in range(nmax):
    
    wn[i]=2*pi*(i+1)/T
    
    val=(1/tau)**2 + wn[i]**2
    
    den=1/val
    
    an[i]=pf*den*1/tau*(1-exp(-T/tau))
    
    bn[i]=pf*wn[i]*den*(1-exp(-T/tau))
    
    
    hn[i,:]=an[i]*cos(wn[i]*t) + bn[i]*sin(wn[i]*t)
    
a0=V/T*(T + tau*exp(-t_e/tau)*exp(-T/tau)-tau*exp(-t_e/tau))

Fourier_dict={}
Fourier_dict["a_0"]=a0
Fourier_dict["a_n"]=an
Fourier_dict["b_n"]=bn
Fourier_dict["harmonics"]=hn
Fourier_dict["omega_n"]=wn
Fourier_dict["n"]=n
Fourier_dict["time"]=t

data_dict["Fourier data"]=Fourier_dict