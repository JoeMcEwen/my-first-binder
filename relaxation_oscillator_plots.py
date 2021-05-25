import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, exp, pi
import ipywidgets as widgets
from ipywidgets import interact, IntSlider, FloatSlider
from relaxation_oscillator_data_gen import data_dict

from bokeh.plotting import figure,show

def make_voltage_plot():
    
    t=data_dict["voltage data"]["time"]
    v=data_dict["voltage data"]["voltage"]
    
    
    tools = "hover, box_zoom, undo, crosshair"
    p=figure(plot_height=400,plot_width=700,x_range=(t[0],t[-1]),tools=tools)
    p.xaxis.axis_label="time"
    p.yaxis.axis_label="voltage"
    p.xaxis.axis_label_text_font_size="20pt"
    p.yaxis.axis_label_text_font_size="20pt"
    p.line(t,v, line_width=4, line_alpha=.8)
    return show(p)

def make_periodic_voltage_plot():
    
    t=data_dict["periodic voltage data"]["time"]
    v=data_dict["periodic voltage data"]["voltage"]
    
    tools = "hover, box_zoom, undo, crosshair"
    p=figure(plot_height=400,plot_width=700,x_range=(t[0],t[-1]),tools=tools)
    p.xaxis.axis_label="time"
    p.yaxis.axis_label="voltage"
    p.xaxis.axis_label_text_font_size="20pt"
    p.yaxis.axis_label_text_font_size="20pt"
    p.line(t,v, line_width=4, line_alpha=.8)
    return show(p)
def plot_neon_interactive(n):
    
    t=data_dict["Fourier data"]["time"]
    hn=data_dict["Fourier data"]["harmonics"]
    
    v=data_dict["periodic voltage data"]["voltage"]
    
    f=np.sum(hn[:n,:],axis=0) + data_dict["Fourier data"]["a_0"]
    
    fig=plt.figure(figsize=(14,6))
    ax=fig.add_subplot(111)
    ax.set_xlim(t[0],t[-1])
    ax.set_ylim(35,90)
    ax.set_xlabel("time",size=20)
    
    label="Fourier approx., n=" + str(n)
    
    ax.plot(t,v,lw=4, alpha=.5, label="voltage")
    ax.plot(t,f,lw=2,alpha=.8,label=label)
    ax.legend(fontsize="xx-large",loc=3)
    ax.grid()
    plt.close()
    
    return fig 
    
def neon_interactive():
    
    nmax=data_dict["Fourier data"]["n"][-1]
    n_widget=IntSlider(value=1,min=1,max=nmax, description="n terms")
     
    return interact(plot_neon_interactive,n=n_widget)