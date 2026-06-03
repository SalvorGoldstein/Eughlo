import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.integrate as inte
from scipy.signal import find_peaks
D = 1.5
sigma = 1
mu =0
deltat=0
Dplus=3
Dmoins=0
pd=1/(Dplus-Dmoins)
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
def pics(x, L, height=None, prominence=2e-48, distance=None):
    peaks, props = find_peaks(L, height=height, prominence=prominence, distance=distance)
    return peaks

def aff(D_val):
    xf= []
    for i in range(100):
        chemin = path(sigma, mu, deltat, D_val)
        t = chemin[0]
        x = chemin[1]
        deltax = chemin[2]
        xf.append(x[len(x)-1])
        plt.plot(t,x)
    xf =np.array(xf)
    #plt.hist(xf,bins = 200,density = True)
    #plt.text(-0.0015, 1100,"variance de la position finale : " +str(np.mean(xf*xf))+" 2Dt="+ str(2*D_val*t[len(x)-1]) )
    plt.show()
    
    #print(np.mean(xf*xf))
    #print(2*D_val*t[len(x)-1])
    return 


def Lfunc(D_val,deltax):
    log_L = np.sum(-0.5 * np.log(4 * np.pi * D_val * deltat)- deltax**2 / (4 * D_val * deltat))
    L=np.exp(log_L)
    return L

def PD(D_val):
    if Dmoins < D_val <Dplus:
        return 1/ (Dplus - Dmoins)
    else:
        return 0





def mult(D_val,deltax):
    return Lfunc(D_val,deltax)*PD(D_val)


def Pdata(Dplus,Dmoins):
    return 





#aff(D)


###########
plt.figure()
D_grid = np.linspace(Dmoins, Dplus, 3000)
y=[]
for i in range(len(D_grid)):
   y.append( mult(D_grid[i],deltax))
y= np.array(y)[1:]
########
dD=(Dplus-Dmoins)/1000
D_grid=D_grid[1:]
PData = np.sum(y*dD) 
print(PData)
print(y)
y = y/PData



plt.plot(D_grid,y)
plt.xlim(Dmoins,Dplus)
plt.xlabel("D (m²/s)")
plt.ylabel("P(D | data)")
plt.title("Posterior P(D|data) ∝ P(data|D) · P(D)")
#plt.savefig()
plt.show()