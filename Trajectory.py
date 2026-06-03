import numpy as np
import matplotlib.pyplot as plt
import random
D = 1e-10
sigma = 1
mu =0
deltat=1
Dplus=3.28e-11
Dmoins=3.28e-12
pd=1/(Dplus-Dmoins)
def path(sigma,mu,deltat,D):
    x = []
    x.append(0)
    deltax = []
    t= []
    t.append(0)
    
    for i in range(1,100):
        eta= random.gauss(mu, sigma)
        t.append(i)
        x.append(x[len(x)-1]+np.sqrt(2*D*deltat)*eta)
        deltax.append(np.sqrt(2*D*deltat)*eta)
    return t,x,np.array(deltax)






def log_Pdata_D(D_val):
    total_log_L = 0.0
    for i in range(1000):
        chemin = path(sigma, mu, deltat, D_val)
        deltax = chemin[2]
        log_L = np.sum(-0.5 * np.log(4 * np.pi * D_val * deltat)- deltax**2 / (4 * D_val * deltat))
        total_log_L += log_L
    return total_log_L



def log_PD(D_val):
    return np.log(1.0 / (Dplus - Dmoins))

y= []
D_grid = np.linspace(Dmoins, Dplus, 300)
for i in range(len(D_grid)):
    y.append(log_Pdata_D(D_grid[i])*log_PD(D_grid[i]))



plt.plot(D_grid, y)

plt.xlabel("D (m²/s)")
plt.ylabel("P(D | data)")
plt.title("Posterior P(D|data) ∝ P(data|D) · P(D)")
plt.tight_layout()
plt.show()