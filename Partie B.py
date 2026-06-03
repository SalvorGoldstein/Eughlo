import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.integrate as inte
from scipy.signal import find_peaks
D = 1.5
sigma = 1
mu =0
deltat=0.003
Dplus=3
Dmoins=0


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

chemin = path(sigma, mu, deltat, D)
deltax = chemin[2]




def Pdata_DPD(D_val,deltax):######Calcul de P  de data sachant D fois P(D)
    log_L = np.sum(-0.5 * np.log(4 * np.pi * D_val * deltat)- deltax**2 / (4 * D_val * deltat))
    L=np.exp(log_L)
    if Dmoins < D_val <Dplus:
        return L/ (Dplus - Dmoins)
    else:
        return 0



def simulateD(D_val):
    xf= []
    for i in range(100):
        chemin = path(sigma, mu, deltat, D)
        x = chemin[1]
        t = chemin[0]
        xf.append(x[len(x)-1]) 
    xf=np.array(xf)
    return np.mean(xf*xf)/(2*t[len(t)-1])





D_grid = np.linspace(Dmoins, Dplus, 1000)
y=[]
for i in range(len(D_grid)):
   y.append( Pdata_DPD(D_grid[i],deltax))
y= np.array(y)[1:]
D_grid=D_grid[1:]
PData = np.trapezoid(y, D_grid)
y = y/PData


#####affichage#########
plt.figure()

for i in range(10):
    plt.axvline(simulateD(D),  linestyle='--')
plt.plot(D_grid,y)
plt.xlim(Dmoins,Dplus)
plt.xlabel("D (m²/s)")
plt.ylabel("P(D | data)")
plt.title("Posterior P(D|data) ∝ P(data|D) · P(D)")
plt.show()