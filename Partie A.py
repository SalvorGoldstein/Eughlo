import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.integrate as inte
from scipy.signal import find_peaks
D = 1.5
sigma = 1
mu =0
deltat=0.003
def path(sigma,mu,deltat,D):
    x = []
    x.append(0)
    deltax = []
    t= []
    tinst =0
    t.append(0)
    for i in range(1,100):
        eta= random.gauss(mu, sigma)
        tinst = tinst + deltat
        t.append(tinst)
        x.append(x[len(x)-1]+np.sqrt(2*D*deltat)*eta)
        deltax.append(np.sqrt(2*D*deltat)*eta)
    return t,x,np.array(deltax)


def xt(D_val):
    for i in range(1000):
        chemin = path(sigma, mu, deltat, D)
        t = chemin[0]
        x = chemin[1]      
        plt.plot(t,x)
    plt.show()
    return

def varxf(D_val):
    xf= []
    for i in range(1000):
        chemin = path(sigma, mu, deltat, D)
        x = chemin[1]
        t = chemin[1]
        xf.append(x[len(x)-1]) 
    xf=np.array(xf)
    plt.hist(xf,bins = 200,density = True)
    plt.text(-0.0015, 1100,"variance de la position finale : " +str(np.mean(xf*xf))+" 2Dt="+ str(2*D*t[len(x)-1]) )
    plt.show()
    return

xt(D)

varxf(D)
